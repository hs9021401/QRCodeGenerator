# 實作計畫 - 匯出個別 PNG 圖片

## Phase 1: 核心邏輯擴充
- [x] Task: 在 `src/qr_generator.py` 中新增 `save_as_png` 或擴充現有邏輯，支援將 QR Code 物件儲存至指定路徑。
- [x] Task: 實作檔名清洗（Sanitize filename）功能，處理非法字元。

## Phase 2: GUI 介面更新
- [x] Task: 在 `src/gui.py` 介面中新增「匯出 PNG 圖片」按鈕。
- [x] Task: 實作按鈕觸發的資料夾選擇邏輯。
- [x] Task: 整合核心邏輯，並加入進度或成功提示。

## Phase 3: 驗證與測試
- [x] Task: 撰寫單元測試驗證檔名清洗邏輯。
- [ ] Task: 手動測試多筆資料匯出，確認檔名正確且無覆蓋問題。
- [ ] Task: 重新打包執行檔。
