import os
import asyncio
import aiohttp
import logging
from typing import Dict, List, Tuple
from aiohttp import ClientTimeout
from tqdm import tqdm
from datetime import datetime
from utils import verify_file_size

class DownloadManager:
    def __init__(self, config: Dict, logger: logging.Logger):
        self.config = config
        self.logger = logger

    async def download_file(self, session: aiohttp.ClientSession, url: str, filename: str, expected_size: float) -> bool:
        """
        Download a file with progress bar, retries and size verification
        """
        retries = self.config['max_retries']
        retry_delay = self.config['retry_delay']
        
        for attempt in range(retries):
            try:
                async with session.get(url) as response:
                    response.raise_for_status()
                    total_size = float(response.headers.get('content-length', 0))
                    
                    # Create progress bar
                    progress = tqdm(
                        total=total_size,
                        unit='B',
                        unit_scale=True,
                        desc=os.path.basename(filename)
                    )
                    
                    # Save the file
                    with open(filename, 'wb') as f:
                        downloaded_size = 0
                        while True:
                            chunk = await response.content.read(self.config['chunk_size'])
                            if not chunk:
                                break
                            f.write(chunk)
                            downloaded_size += len(chunk)
                            progress.update(len(chunk))
                    
                    progress.close()
                    
                    # Verify file size
                    if not verify_file_size(downloaded_size, expected_size):
                        self.logger.warning(f"Size mismatch for {filename}: Expected {expected_size}MB, got {downloaded_size/1024/1024:.2f}MB")
                        raise ValueError("File size verification failed")
                    
                    self.logger.info(f"Successfully downloaded: {filename}")
                    return True
                    
            except Exception as e:
                self.logger.error(f"Error downloading {filename} (attempt {attempt + 1}/{retries}): {str(e)}")
                if attempt < retries - 1:
                    await asyncio.sleep(retry_delay)
                else:
                    return False
        
        return False

    async def download_files(self, files: List[Dict], folder_name: str) -> Tuple[int, int]:
        """Download multiple files concurrently with progress tracking"""
        timeout = ClientTimeout(total=self.config['timeout'])
        connector = aiohttp.TCPConnector(limit=self.config['max_concurrent'])
        
        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
            tasks = []
            for file in files:
                filename = os.path.join(folder_name, file['name'])
                task = asyncio.ensure_future(
                    self.download_file(
                        session, 
                        file['url'], 
                        filename,
                        file['size']
                    )
                )
                tasks.append(task)
                
            results = await asyncio.gather(*tasks)
            successful = sum(1 for r in results if r)
            return successful, len(files)

    async def process_json_data(self, json_data: Dict) -> None:
        """Process the JSON data and download files"""
        self.logger.info("Starting download process")
        
        if not json_data['list']:
            raise ValueError("No items found in the JSON data")
        
        folder_name = json_data['name']
        self.logger.info(f"Creating directory: {folder_name}")
        
        # Create directory if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        # Prepare download list
        files = [{
            'url': item['resource_url'],
            'name': f"{item['resource_name']}.mp3",
            'size': item['resource_size']
        } for item in json_data['list']]
        
        # Download files
        start_time = datetime.now()
        successful, total = await self.download_files(files, folder_name)
        duration = (datetime.now() - start_time).total_seconds()
        
        # Log results
        self.logger.info(f"Download complete! Successfully downloaded {successful} of {total} files")
        self.logger.info(f"Total time: {duration:.2f} seconds")