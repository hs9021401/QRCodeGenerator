import sys
import os

# 將 src 加入模組搜尋路徑
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.utils.logger import setup_logger
from src.gui import App

def main():
    # 初始化 Logger
    logger = setup_logger()
    logger.info("應用程式啟動中...")
    
    try:
        # 啟動 GUI
        app = App()
        app.mainloop()
    except Exception as e:
        logger.exception("應用程式執行時發生未預期錯誤")
        raise

if __name__ == "__main__":
    main()