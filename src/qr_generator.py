import qrcode
from PIL import Image, ImageDraw, ImageFont
import logging

logger = logging.getLogger(__name__)

class QRGenerator:
    """處理 QR Code 產生、縮放與文字標籤整合的類別"""
    
    # 300 DPI 下，1英吋 = 2.54公分 = 300像素
    # 1公分 = 300 / 2.54 ≈ 118.11 像素
    DPI = 300
    PX_PER_CM = DPI / 2.54

    def __init__(self):
        self.error_levels = {
            "L": qrcode.constants.ERROR_CORRECT_L,
            "M": qrcode.constants.ERROR_CORRECT_M,
            "Q": qrcode.constants.ERROR_CORRECT_Q,
            "H": qrcode.constants.ERROR_CORRECT_H,
        }

    @staticmethod
    def sanitize_filename(text):
        """
        清洗文字使其符合 Windows 檔名規則
        """
        import re
        # Windows 不允許字元: \ / : * ? " < > |
        # 同時移除換行符號
        clean_text = re.sub(r'[\\/:*?"<>|]', '_', text)
        clean_text = clean_text.replace('\n', '_').replace('\r', '')
        # 限制長度，避免過長檔名問題
        return clean_text[:150].strip()

    def generate(self, text, size_cm=None, error_correction="Q"):
        """
        產生包含文字標籤的 QR Code 圖片
        :param text: 內容文字
        :param size_cm: 輸出的實際尺寸 (公分)
        :param error_correction: 容錯等級 (L, M, Q, H)
        :return: PIL Image 物件
        """
        logger.info(f"產生圖文整合 QR Code: '{text[:20]}...', 尺寸: {size_cm}cm")
        
        # 1. 產生基礎 QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=self.error_levels.get(error_correction.upper(), qrcode.constants.ERROR_CORRECT_Q),
            box_size=10,
            border=2, # 縮小邊界以利排版
        )
        qr.add_data(text)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        # 2. 準備整合文字
        # 預留文字空間 (約為圖片高度的 15%)
        qr_w, qr_h = qr_img.size
        text_padding = int(qr_h * 0.15)
        combined_img = Image.new('RGB', (qr_w, qr_h + text_padding), color='white')
        combined_img.paste(qr_img, (0, 0))

        # 3. 繪製文字
        draw = ImageDraw.Draw(combined_img)
        # 嘗試加載字體，若失敗則使用預設
        try:
            # Windows 常見字體路徑
            font_size = int(text_padding * 0.8)
            font = ImageFont.truetype("msjh.ttc", font_size) # 微軟正黑體
        except:
            font = ImageFont.load_default()

        # 計算文字置中位置
        # 使用 textbbox 獲取文字範圍 (Pillow 9.2+)
        left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
        text_w = right - left
        text_x = (qr_w - text_w) // 2
        text_y = qr_h + (text_padding - (bottom - top)) // 2 - top
        
        draw.text((text_x, text_y), text, fill="black", font=font)

        # 4. 縮放至指定公分尺寸
        if size_cm:
            target_px = int(size_cm * self.PX_PER_CM)
            # 保持比例縮放，以寬度為準
            combined_img = combined_img.resize((target_px, int(target_px * (combined_img.height / combined_img.width))), Image.Resampling.LANCZOS)
        
        return combined_img