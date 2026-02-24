import pytest
from src.word_generator import WordGenerator
from docx import Document
import os

def test_word_creation_and_table():
    output_path = "tests/test_output.docx"
    if os.path.exists(output_path):
        os.remove(output_path)
        
    generator = WordGenerator()
    data_list = [
        {"text": "A001", "img_path": "tests/dummy_qr.png"},
        {"text": "A002", "img_path": "tests/dummy_qr.png"}
    ]
    
    # 建立一個測試用的圖片
    from PIL import Image
    Image.new('RGB', (100, 100), color='black').save("tests/dummy_qr.png")
    
    generator.create_report(data_list, qr_size_cm=2.0, output_path=output_path)
    
    assert os.path.exists(output_path)
    doc = Document(output_path)
    
    # 驗證是否有表格產生
    assert len(doc.tables) > 0
    
    # 清理
    if os.path.exists(output_path):
        os.remove(output_path)
    if os.path.exists("tests/dummy_qr.png"):
        os.remove("tests/dummy_qr.png")

def test_calculate_columns():
    generator = WordGenerator()
    # A4 寬度約 21cm，扣除邊距 (假設左右各 1cm) 剩下 19cm
    # 如果 QR Code 尺寸是 4cm，預期 19 // 4 = 4 欄 (忽略間距情況下)
    cols = generator.calculate_max_columns(qr_size_cm=4.0, page_width_cm=21.0, margin_cm=1.0)
    assert cols == 4
