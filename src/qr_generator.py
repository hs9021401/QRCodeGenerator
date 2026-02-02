import qrcode
from PIL import Image
import logging

logger = logging.getLogger(__name__)

class QRGenerator:
    """處理 QR Code 產生與縮放的類別"""
    
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

    def generate(self, text, size_cm=None, error_correction="Q"):
        """
        產生 QR Code 圖片
        :param text: 內容文字
        :param size_cm: 輸出的實際尺寸 (公分)
        :param error_correction: 容錯等級 (L, M, Q, H)
        :return: PIL Image 物件
        """
        logger.info(f"產生 QR Code: '{text[:20]}...', 尺寸: {size_cm}cm, 容錯: {error_correction}")
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=self.error_levels.get(error_correction.upper(), qrcode.constants.ERROR_CORRECT_Q),
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        if size_cm:
            target_px = int(size_cm * self.PX_PER_CM)
            img = img.resize((target_px, target_px), Image.Resampling.LANCZOS)
            logger.debug(f"圖片縮放至 {target_px}x{target_px} 像素")

        return img
