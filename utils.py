import json
from typing import Dict

async def read_json_file(filename: str) -> Dict:
    """Read and parse JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        raise
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {str(e)}")
        raise
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        raise

def verify_file_size(actual_size: int, expected_size: float, tolerance: float = 0.1) -> bool:
    """Verify if the actual file size matches the expected size (in MB)"""
    actual_mb = actual_size / 1024 / 1024
    return abs(actual_mb - expected_size) <= tolerance