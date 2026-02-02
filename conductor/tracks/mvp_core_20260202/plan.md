# 實作計畫 - MVP 核心功能與 GUI 介面

## Phase 1: 環境搭建與基礎邏輯
- [x] Task: 使用 uv 初始化專案並安裝依賴 (qrcode, python-docx, Pillow, CustomTkinter)
- [x] Task: 建立基礎專案結構與 Logging 設定
- [~] Task: Conductor - User Manual Verification 'Phase 1: 環境搭建與基礎邏輯' (Protocol in workflow.md)

## Phase 2: QR Code 產生邏輯 (TDD)
- [ ] Task: 編寫 QR Code 產生邏輯的單元測試
- [ ] Task: 實作 QR Code 產生功能（包含尺寸轉換與容錯設定）
- [ ] Task: Conductor - User Manual Verification 'Phase 2: QR Code 產生邏輯 (TDD)' (Protocol in workflow.md)

## Phase 3: Word 文件排版邏輯 (TDD)
- [ ] Task: 編寫 Word 表格佈局邏輯的單元測試
- [ ] Task: 實作 A4 頁面佈局與表格插入功能（參考 BBPO.doc）
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Word 文件排版邏輯 (TDD)' (Protocol in workflow.md)

## Phase 4: GUI 介面開發
- [ ] Task: 使用 CustomTkinter 建立主視窗與文字輸入區域
- [ ] Task: 實作檔案讀取與參數設定功能 (尺寸、匯出路徑)
- [ ] Task: 整合 GUI 與核心產生邏輯
- [ ] Task: Conductor - User Manual Verification 'Phase 4: GUI 介面開發' (Protocol in workflow.md)

## Phase 5: 打包與最終驗證
- [ ] Task: 使用 PyInstaller 設定打包參數
- [ ] Task: 執行單一執行檔封裝
- [ ] Task: 進行跨環境手動驗證
- [ ] Task: Conductor - User Manual Verification 'Phase 5: 打包與最終驗證' (Protocol in workflow.md)