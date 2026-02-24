# QRCodeGenerator

一個使用 Python 開發的現代化桌面應用程式，用於批次產生 QR Code 圖片，並支援匯入 Word 文件排版或個別導出為 PNG 圖檔。

![Version](https://img.shields.io/badge/version-v2.0.20260224-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 核心功能

- **批次產生**：支援一次輸入多行文字，每行產生一個獨立的 QR Code。
- **Word 整合**：參考 `BBPO.doc` 格式，自動將 QR Code 排列插入 Word 表格中，並附加文字標籤。
- **PNG 個別匯出**：支援將所有 QR Code 儲存為獨立的 PNG 圖片，具備：
    - **檔名清洗**：自動處理 Windows 不合法字元。
    - **自動去重**：內容重複時自動加上序號避免覆蓋。
- **現代化 UI**：使用 `CustomTkinter` 打造，支援 DPI 高清感知與系統深淺色模式。
- **自定義尺寸**：可自由設定 QR Code 的輸出尺寸（公分）。

## 技術堆疊

- **GUI 框架**：[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- **環境管理**：[uv](https://github.com/astral-sh/uv)
- **QR Code 產生**：`qrcode`
- **影像處理**：`Pillow` (PIL)
- **文件操作**：`python-docx`
- **封裝工具**：`PyInstaller`

## 開發環境設定

本專案使用 `uv` 進行依賴管理，確保開發環境的一致性。

1. **安裝 uv** (如果尚未安裝):
   ```powershell
   powershell -c "ir | iex" # Windows
   ```

2. **同步環境與安裝依賴**:
   ```powershell
   uv sync
   ```

3. **執行程式**:
   ```powershell
   uv run python main.py
   ```

4. **執行測試**:
   ```powershell
   uv run python tests/test_filename_sanitize.py
   ```

## 打包教學

專案已配置好 `.spec` 檔案，可直接使用以下指令打包成單一執行檔（已包含自定義圖示與相關資源）：

```powershell
uv run pyinstaller --clean QRCodeGenerator.spec
```

打包完成後的執行檔位於 `dist/QRCodeGenerator.exe`。

## 專案結構

- `src/`: 原始碼
    - `gui.py`: 主視窗邏輯與 UI
    - `qr_generator.py`: QR Code 產生與檔名清洗邏輯
    - `word_generator.py`: Word 表格排版邏輯
- `conductor/`: 專案管理軌跡與計畫文件
- `tests/`: 單元測試
- `dist/`: 產出的執行檔
- `QRCodeGenerator.spec`: PyInstaller 打包設定

## 作者

Designed by Alex Lin
