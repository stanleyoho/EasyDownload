# Async File Downloader

一個基於 Python 非同步（async）的文件下載器，支持並發下載、進度顯示、錯誤重試等功能。

## 功能特點

- 非同步並發下載
- 實時進度顯示
- 自動重試機制
- 文件大小驗證
- 詳細的日誌記錄
- 可配置的下載參數

## 環境需求

- Python 3.8 或更高版本
- 虛擬環境（推薦使用 venv）

## 快速開始

### 1. 克隆專案

```bash
git clone <your-repository-url>
cd test_download
```

### 2. 創建並啟動虛擬環境

```bash
# 創建虛擬環境
python3 -m venv venv

# 啟動虛擬環境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. 安裝依賴

```bash
pip install -r requirements.txt
```

### 4. 配置檔案

1. 配置下載參數 (config.json):
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

2. 準備下載清單 (data.json):
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

### 5. 執行程式

```bash
python main.py
```

## 配置說明

### config.json 參數

- `chunk_size`: 下載區塊大小（bytes）
- `max_retries`: 下載失敗重試次數
- `retry_delay`: 重試等待時間（秒）
- `timeout`: 下載超時時間（秒）
- `max_concurrent`: 最大並發下載數
- `logging.level`: 日誌級別（INFO/DEBUG/WARNING/ERROR）
- `logging.file`: 日誌文件名稱

### data.json 格式

- `name`: 下載文件夾名稱
- `list`: 下載文件列表
  - `resource_url`: 文件下載網址
  - `resource_name`: 文件名稱
  - `resource_size`: 預期文件大小（MB）

## 專案結構

```
test_download/
├── config.json         # 配置文件
├── data.json          # 下載清單
├── requirements.txt   # 依賴套件
├── main.py           # 主程式入口
├── config.py         # 配置管理
├── logger.py         # 日誌管理
├── utils.py          # 工具函數
└── download_manager.py # 下載核心功能
```

## 開發說明

### 添加新功能

1. 在相應的模組中添加功能
2. 更新配置文件（如需要）
3. 更新文檔

### 代碼風格

- 遵循 PEP 8 規範
- 使用類型提示
- 添加適當的註釋和文檔字符串

## 常見問題

1. Q: 下載失敗怎麼辦？
   A: 程式會自動重試，重試次數可在 config.json 中配置

2. Q: 如何修改並發數？
   A: 在 config.json 中修改 max_concurrent 參數

3. Q: 下載速度很慢怎麼辦？
   A: 可以調整 chunk_size 和 max_concurrent 參數

## 貢獻指南

歡迎提交 Pull Request 或建立 Issue。

## 授權

MIT License