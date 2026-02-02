import customtkinter as ctk
import os
import logging
from tkinter import filedialog, messagebox
from src.qr_generator import QRGenerator
from src.word_generator import WordGenerator
import tempfile
import shutil

logger = logging.getLogger(__name__)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR Code 批量產生與文件整合工具")
        self.geometry("800x600")
        
        # 設定外觀
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # UI 組件
        self.setup_ui()
        
        self.qr_gen = QRGenerator()
        self.word_gen = WordGenerator()

    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # 頂部標題與說明
        self.header_label = ctk.CTkLabel(self, text="QR Code 批量產生工具", font=ctk.CTkFont(size=20, weight="bold"))
        self.header_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # 中間區域：文字輸入
        self.textbox_frame = ctk.CTkFrame(self)
        self.textbox_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.textbox_frame.grid_columnconfigure(0, weight=1)
        self.textbox_frame.grid_rowconfigure(1, weight=1)

        self.input_label = ctk.CTkLabel(self.textbox_frame, text="請輸入文字 (每一行代表一個 QR Code):")
        self.input_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.input_text = ctk.CTkTextbox(self.textbox_frame)
        self.input_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # 右側/下方區域：設定與按鈕
        self.controls_frame = ctk.CTkFrame(self)
        self.controls_frame.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.controls_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # 尺寸設定
        self.size_label = ctk.CTkLabel(self.controls_frame, text="QR Code 尺寸 (cm):")
        self.size_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.size_entry = ctk.CTkEntry(self.controls_frame)
        self.size_entry.insert(0, "2.5")
        self.size_entry.grid(row=0, column=1, padx=10, pady=10)

        # 檔案操作按鈕
        self.load_button = ctk.CTkButton(self.controls_frame, text="讀取文字檔 (.txt)", command=self.load_file)
        self.load_button.grid(row=1, column=0, padx=10, pady=10)

        self.generate_button = ctk.CTkButton(self.controls_frame, text="產生 Word 文件", command=self.generate, fg_color="green", hover_color="#006400")
        self.generate_button.grid(row=1, column=1, padx=10, pady=10)

        # 狀態列
        self.status_label = ctk.CTkLabel(self, text="就緒", anchor="w")
        self.status_label.grid(row=3, column=0, padx=20, pady=(0, 5), sticky="ew")

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    self.input_text.delete("1.0", "end")
                    self.input_text.insert("1.0", content)
                self.set_status(f"已讀取檔案: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("錯誤", f"無法讀取檔案: {e}")

    def set_status(self, text):
        self.status_label.configure(text=text)
        logger.info(text)

    def generate(self):
        lines = self.input_text.get("1.0", "end-1c").splitlines()
        lines = [line.strip() for line in lines if line.strip()]

        if not lines:
            messagebox.showwarning("警告", "請輸入至少一行文字內容。")
            return

        try:
            qr_size = float(self.size_entry.get())
        except ValueError:
            messagebox.showerror("錯誤", "尺寸必須是數字。")
            return

        # 選擇儲存位置
        output_path = filedialog.asksaveasfilename(
            defaultextension=".docx",
            filetypes=[("Word Document", "*.docx")],
            initialfile=f"QR_Report_{os.path.basename(os.getcwd())}.docx"
        )
        
        if not output_path:
            return

        self.set_status("處理中，請稍候...")
        self.update()

        temp_dir = tempfile.mkdtemp()
        try:
            data_list = []
            for i, text in enumerate(lines):
                img = self.qr_gen.generate(text, size_cm=qr_size)
                img_path = os.path.join(temp_dir, f"qr_{i}.png")
                img.save(img_path)
                data_list.append({"text": text, "img_path": img_path})

            self.word_gen.create_report(data_list, qr_size, output_path)
            self.set_status(f"完成！文件已儲存至: {output_path}")
            messagebox.showinfo("成功", f"文件已成功產生並儲存至：\n{output_path}")
        except Exception as e:
            logger.exception("產生過程中發生錯誤")
            messagebox.showerror("錯誤", f"產生過程中發生錯誤: {e}")
            self.set_status("產生失敗")
        finally:
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    app = App()
    app.mainloop()
