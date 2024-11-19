# timer_widget.py
import tkinter as tk
from tkinter import ttk
import time

class TimerWidget(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.timer_running = False
        self.start_time = 0
        self.setup_timer()
        
    def setup_timer(self):
        self.timer_label = ttk.Label(self, text="00:00:00")
        self.timer_label.pack()
        
        self.start_button = ttk.Button(self, text="Start", command=self.start_timer)
        self.start_button.pack(side="left")
        
        self.stop_button = ttk.Button(self, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side="left")

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = time.time()
            self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            m, s = divmod(int(elapsed_time), 60)
            h, m = divmod(m, 60)
            time_str = f"{h:02}:{m:02}:{s:02}"
            self.timer_label.config(text=time_str)
            self.after(1000, self.update_timer)