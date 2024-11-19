# progress_widget.py
import tkinter as tk
from tkinter import ttk

class ProgressWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_progress()
        
    def setup_progress(self):
        self.progress = ttk.Progressbar(self, orient="horizontal", 
                                      length=200, mode="determinate")
        self.progress.pack(pady=10)