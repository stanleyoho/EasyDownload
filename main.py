import asyncio
import logging
from config import Config
from logger import Logger
from utils import read_json_file
from download_manager import DownloadManager

async def main():
    """Main application entry point"""
    try:
        # Initialize configuration
        config = Config()
        
        # Setup logging
        logger = Logger.setup_logging(config.get_logging_config())
        
        # Load download configuration
        download_config = config.get_download_config()
        
        # Create download manager
        downloader = DownloadManager(download_config, logger)
        
        # Read input data
        print("Reading download data...")
        json_data = await read_json_file('data.json')
        
        # Start download process
        print("Starting downloads...")
        await downloader.process_json_data(json_data)
        
    except Exception as e:
        logging.error(f"Application error: {str(e)}")
        raise

if __name__ == "__main__":
    asyncio.run(main())