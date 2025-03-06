import json
from typing import Dict

class Config:
    def __init__(self, config_file: str = 'config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self) -> Dict:
        """Load configuration from config.json"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {str(e)}, using defaults")
            return {
                "download": {
                    "chunk_size": 32768,
                    "max_retries": 3,
                    "retry_delay": 1,
                    "timeout": 300,
                    "max_concurrent": 10
                },
                "logging": {
                    "enabled": True,
                    "level": "INFO",
                    "file": "download.log"
                }
            }

    def get_download_config(self) -> Dict:
        return self.config['download']

    def get_logging_config(self) -> Dict:
        return self.config['logging']
