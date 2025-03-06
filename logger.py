import logging
from typing import Dict

class Logger:
    @staticmethod
    def setup_logging(config: Dict) -> logging.Logger:
        """Setup logging configuration and return logger instance"""
        if config['enabled']:
            logging.basicConfig(
                level=getattr(logging, config['level']),
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.FileHandler(config['file']),
                    logging.StreamHandler()
                ]
            )
        
        logger = logging.getLogger('downloader')
        return logger