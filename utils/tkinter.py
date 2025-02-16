import tkinter as tk
from tkinter import ttk
from utils.validations import Validations

class TkinterUtils(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the parent tk.Tk class
        self.v = Validations()
        self.tk = tk
        
        self.initialize_window()
    
    def initialize_window(self):
        """Initialize the main window and its components"""
        # Configure main window
        self.title("Event Management System")
        self.geometry("400x300")
        
        # Create main container
        self.main_frame = ttk.Frame(self, padding="20")
        self.main_frame.pack(expand=True)

    def create_form_field(self, parent, label_text, show=None):
        """Helper method to create form fields with labels"""
        ttk.Label(parent, text=label_text).pack()
        var = tk.StringVar()
        entry = ttk.Entry(parent, textvariable=var, show=show)
        entry.pack(pady=5, fill='x')
        return var
    
    def create_form_frame(self, title):
        """Helper method to create a form frame"""
        self.main_frame.pack_forget()
        frame = ttk.Frame(self, padding="20")
        frame.pack(expand=True)
        ttk.Label(frame, text=title, font=("Arial", 12, "bold")).pack(pady=10)
        return frame