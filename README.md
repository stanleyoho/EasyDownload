# Async File Downloader

A Python-based asynchronous file downloader that supports concurrent downloads, progress display, error retry, and more features.

## Features

- Asynchronous concurrent downloads
- Real-time progress display
- Automatic retry mechanism
- File size validation
- Detailed logging
- Configurable download parameters

## Requirements

- Python 3.8 or higher
- Virtual environment (venv recommended)

## Quick Start

### 1. Clone the Project

```bash
git clone <your-repository-url>
cd test_download
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configuration Files

1. Configure download parameters (config.json):
```json
{
    "download": {
        "chunk_size": 32768,
        "max_retries": 3,
        "retry_delay": 1,
        "timeout": 300,
        "max_concurrent": 10
    },
    "logging": {
        "enabled": true,
        "level": "INFO",
        "file": "download.log"
    }
}
```

2. Prepare download list (data.json):
```json
{
    "name": "download_folder_name",
    "list": [
        {
            "resource_url": "https://example.com/file1.mp3",
            "resource_name": "file1",
            "resource_size": 1.5
        }
    ]
}
```

### 5. Run the Program

```bash
python main.py
```

## Configuration Guide

### config.json Parameters

- `chunk_size`: Download block size (bytes)
- `max_retries`: Number of download retry attempts
- `retry_delay`: Wait time between retries (seconds)
- `timeout`: Download timeout (seconds)
- `max_concurrent`: Maximum concurrent downloads
- `logging.level`: Log level (INFO/DEBUG/WARNING/ERROR)
- `logging.file`: Log file name

### data.json Format

- `name`: Download folder name
- `list`: Download file list
  - `resource_url`: File download URL
  - `resource_name`: File name
  - `resource_size`: Expected file size (MB)

## Project Structure

```
test_download/
├── config.json         # Configuration file
├── data.json          # Download list
├── requirements.txt   # Dependencies
├── main.py           # Main program entry
├── config.py         # Configuration management
├── logger.py         # Logging management
├── utils.py          # Utility functions
└── download_manager.py # Core download functionality
```

## Development Guide

### Adding New Features

1. Add functionality in the appropriate module
2. Update configuration files (if needed)
3. Update documentation

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Add appropriate comments and docstrings

## FAQ

1. Q: What to do if download fails?
   A: The program will automatically retry, retry count can be configured in config.json

2. Q: How to modify concurrent downloads?
   A: Modify the max_concurrent parameter in config.json

3. Q: What to do if download speed is slow?
   A: Adjust chunk_size and max_concurrent parameters

## Contributing

Pull requests and issues are welcome.

## License

MIT License