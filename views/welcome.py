from utils.tkinter import TkinterUtils
from tkinter import messagebox

class WelcomeView(TkinterUtils):
    def __init__(self):
        super().__init__()
        self.selected_option = None
        self.login_data = None
        
        # Welcome label
        self.tk.Label(
            self.main_frame,
            text="Welcome to the Event Management System",
            font=("Arial", 12, "bold")
        ).pack(pady=20)
        
        # Buttons
        self.tk.Button(
            self.main_frame,
            text="Login",
            command=self.show_login
        ).pack(pady=5, fill='x')
        
        self.tk.Button(
            self.main_frame,
            text="Register User",
            command=self.show_register
        ).pack(pady=5, fill='x')
        
        self.tk.Button(
            self.main_frame,
            text="Exit",
            command=exit
        ).pack(pady=5, fill='x')

    def menu(self) -> int:
        self.mainloop()
        return self.selected_option
    
    def return_option(self, option):
        self.selected_option = option
        self.quit()

    def validate_common_fields(self, email, password):
        """Common validation logic for forms"""
        if not email or not password:
            messagebox.showerror("Error", "All fields are required")
            return False
        if not self.v.validate_email(email):
            messagebox.showerror("Error", "Invalid email format")
            return False
        if not self.v.validate_password(password):
            messagebox.showerror("Error", "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number")
            return False
        return True

    def show_login(self):
        login_frame = self.create_form_frame("LOGIN")
        
        email_var = self.create_form_field(login_frame, "EMAIL:")
        password_var = self.create_form_field(login_frame, "PASSWORD:", show="*")
        
        def submit_login():
            email = email_var.get().strip()
            password = password_var.get()
            
            if self.validate_common_fields(email, password):
                self.login_data = {
                    'email': email,
                    'password': password
                }
                self.selected_option = 1
                self.quit()
        
        self.tk.Button(login_frame, text="LOGIN", command=submit_login).pack(pady=10)
        self.tk.Button(login_frame, text="BACK", command=lambda: self.show_main_menu(login_frame)).pack()

    def show_register(self):
        register_frame = self.create_form_frame("REGISTER")
        
        email_var = self.create_form_field(register_frame, "EMAIL:")
        password_var = self.create_form_field(register_frame, "PASSWORD:", show="*")
        password_confirmation_var = self.create_form_field(register_frame, "CONFIRM PASSWORD:", show="*")
        
        def submit_register():
            email = email_var.get().strip()
            password = password_var.get()
            password_confirmation = password_confirmation_var.get()
            
            if not self.validate_common_fields(email, password):
                return
                
            if password != password_confirmation:
                messagebox.showerror("Error", "Passwords do not match")
                return
                
            self.login_data = {
                'email': email,
                'password': password
            }
            self.selected_option = 2
            self.quit()
        
        self.tk.Button(register_frame, text="REGISTER", command=submit_register).pack(pady=10)
        self.tk.Button(register_frame, text="BACK", command=lambda: self.show_main_menu(register_frame)).pack()

    def show_main_menu(self, current_frame):
        current_frame.destroy()
        self.main_frame.pack(expand=True)

    def login(self) -> dict:
        return self.login_data