import pytest
from PIL import Image
from src.qr_generator import QRGenerator
import os

def test_qr_generation_success():
    generator = QRGenerator()
    # 測試文字產生，預設容錯 Q
    img = generator.generate("Hello World")
    assert isinstance(img, Image.Image)

def test_qr_scaling_cm():
    generator = QRGenerator()
    # 測試縮放到 2x2 cm (在 300 DPI 下，1cm 約 118 像素)
    # 2cm 預期約 236 像素
    size_cm = 2.0
    img = generator.generate("Test Size", size_cm=size_cm)
    
    # 允許正負 2 像素的誤差
    expected_px = int(size_cm * 118.11)
    assert abs(img.width - expected_px) <= 2
    assert abs(img.height - expected_px) <= 2

def test_qr_error_correction():
    import qrcode
    generator = QRGenerator()
    # 驗證容錯率是否生效
    img = generator.generate("Error Test", error_correction="H")
    assert isinstance(img, Image.Image)
