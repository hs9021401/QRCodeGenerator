import os
import sys

# 將專案根目錄加入路徑
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.qr_generator import QRGenerator

def test_sanitize_filename():
    gen = QRGenerator()
    
    # 測試非法字元
    assert gen.sanitize_filename("hello/world") == "hello_world"
    # 使用單引號包裹含有雙引號的字串
    assert gen.sanitize_filename('a:b*c?d"e<f>g|h') == "a_b_c_d_e_f_g_h"
    
    # 測試換行符號
    assert gen.sanitize_filename("line1\nline2") == "line1_line2"
    
    # 測試極長字串
    long_text = "a" * 200
    assert len(gen.sanitize_filename(long_text)) == 150
    
    # 測試空白
    assert gen.sanitize_filename("  test  ") == "test"
    
    print("Sanitize filename tests passed!")

if __name__ == "__main__":
    test_sanitize_filename()
