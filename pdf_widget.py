# pdf_widget.py
import tkinter as tk
from tkinter import ttk, filedialog

class PDFWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_pdf_upload()
        
    def setup_pdf_upload(self):
        self.upload_button = ttk.Button(self, text="Upload PDF", command=self.upload_pdf)
        self.upload_button.pack(pady=10)
        
    def upload_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            print(f"Selected PDF: {file_path}")