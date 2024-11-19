# assignment_tracker.py
import tkinter as tk
from tkinter import ttk
from timer_widget import TimerWidget
from checklist_widget import ChecklistWidget
from pdf_widget import PDFWidget
from progress_widget import ProgressWidget

class AssignmentTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Assignment Tracker")
        self.attributes("-topmost", True)
        self.geometry("300x400")
        
        self.subgoals = [
            "Research Topic",
            "Create Outline",
            "Write Introduction",
            "Body Paragraph 1",
            "Body Paragraph 2",
            "Conclusion",
            "Proofread"
        ]
        
        self.create_widgets()
        
    def create_widgets(self):
        self.pdf_widget = PDFWidget(self)
        self.pdf_widget.pack(pady=10)
        
        self.checklist = ChecklistWidget(self, self.subgoals)
        self.checklist.pack(pady=10)
        
        self.progress = ProgressWidget(self)
        self.progress.pack(pady=10)
        
        self.timer = TimerWidget(self)
        self.timer.pack(pady=10)

    def update_progress(self, value):
        self.progress.progress["value"] = value

if __name__ == "__main__":
    app = AssignmentTracker()
    app.mainloop()