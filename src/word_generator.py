from docx import Document
from docx.shared import Cm, Inches
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os
import logging

logger = logging.getLogger(__name__)

class WordGenerator:
    """處理 Word 文件排版與產出的類別"""

    def __init__(self):
        self.PAGE_WIDTH_CM = 21.0
        self.MARGIN_CM = 1.27

    def calculate_max_columns(self, qr_size_cm, page_width_cm=21.0, margin_cm=1.27):
        available_width = page_width_cm - (margin_cm * 2)
        cols = int(available_width / (qr_size_cm + 0.1))
        return max(1, cols)

    def create_report(self, data_list, qr_size_cm, output_path):
        """
        建立包含整合 QR Code 圖片的 Word 文件
        """
        logger.info(f"開始建立 Word 文件: {output_path}")
        doc = Document()

        section = doc.sections[0]
        section.page_height = Cm(29.7)
        section.page_width = Cm(21.0)
        section.left_margin = Cm(self.MARGIN_CM)
        section.right_margin = Cm(self.MARGIN_CM)
        section.top_margin = Cm(self.MARGIN_CM)
        section.bottom_margin = Cm(self.MARGIN_CM)

        num_cols = self.calculate_max_columns(qr_size_cm, self.PAGE_WIDTH_CM, self.MARGIN_CM)
        num_items = len(data_list)
        # 現在每個 QR Code 僅佔用一列一格
        num_rows = (num_items + num_cols - 1) // num_cols

        table = doc.add_table(rows=num_rows, cols=num_cols)
        table.alignment = WD_ALIGN_PARAGRAPH.CENTER

        for i, item in enumerate(data_list):
            row_idx = i // num_cols
            col_idx = i % num_cols
            
            cell = table.cell(row_idx, col_idx)
            paragraph = cell.paragraphs[0]
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = paragraph.add_run()
            # 插入整合後的圖片
            run.add_picture(item["img_path"], width=Cm(qr_size_cm))
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        doc.save(output_path)
        logger.info(f"Word 文件儲存成功: {output_path}")