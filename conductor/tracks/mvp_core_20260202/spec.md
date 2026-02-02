# 規格書 - MVP 核心功能與 GUI 介面

## 1. 概述
本軌跡旨在建立一個最小可行性產品 (MVP)，讓使用者能透過 GUI 介面輸入文字清單，並產出一份符合 A4 排版、包含 QR Code 與文字標籤的 Word 文件。

## 2. 需求細節
- **輸入**: 支援手動輸入多行文字或讀取 .txt 檔案。
- **QR Code**:
    - 使用 `qrcode` 庫產生。
    - 容錯等級預設為 Q。
    - 使用者可指定列印尺寸 (cm x cm)。
- **Word 輸出**:
    - 使用 `python-docx` 產生。
    - A4 紙張佈局，自動計算每列可容納的 QR Code 數量。
    - 樣式參考 `BBPO.doc` (表格形式)。
- **封裝**: 使用 PyInstaller 打包成單一 .exe 執行檔。

## 3. 驗證標準
- 產生的 QR Code 掃描後文字內容正確。
- Word 文件中的 QR Code 尺寸符合設定。
- 在未安裝 Office 的 Windows 環境下可獨立執行。
