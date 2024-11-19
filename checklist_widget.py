# checklist_widget.py
import tkinter as tk
from tkinter import ttk

class ChecklistWidget(ttk.Frame):
    def __init__(self, parent, subgoals):
        super().__init__(parent)
        self.parent = parent
        self.vars = []
        self.subgoals = subgoals
        self.setup_checklist()
        
    def setup_checklist(self):
        for subgoal in self.subgoals:
            var = tk.IntVar()
            self.vars.append(var)
            checkbox = ttk.Checkbutton(self, text=subgoal, 
                                     variable=var, 
                                     command=self.on_checkbox_change)
            checkbox.pack(anchor="w")
    
    def on_checkbox_change(self):
        completed = sum(var.get() for var in self.vars)
        total = len(self.subgoals)
        progress = (completed / total) * 100
        self.parent.update_progress(progress)