import customtkinter as ctk
from tkinter import messagebox
from screens.dashboard import Dashboard


class LoginWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Medical Store Management System")
        self.geometry("1000x600")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="🏥 Medical Store Management System",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=30)

        # ==========================
        # Username Label
        # ==========================

        username_label = ctk.CTkLabel(
            self,
            text="Username",
            font=("Arial",16,"bold")
        )

        username_label.pack()

        self.username = ctk.CTkEntry(
            self,
            width=320,
            placeholder_text="Enter Username"
        )

        self.username.pack(pady=10)

        # ==========================
        # Password Label
        # ==========================

        password_label = ctk.CTkLabel(
            self,
            text="Password",
            font=("Arial",16,"bold")
        )

        password_label.pack()

        self.password = ctk.CTkEntry(
            self,
            width=320,
            placeholder_text="Enter Password",
            show="*"
        )

        self.password.pack(pady=10)

        # ==========================
        # Show Password
        # ==========================

        self.show_password = ctk.BooleanVar()

        checkbox = ctk.CTkCheckBox(
            self,
            text="Show Password",
            variable=self.show_password,
            command=self.toggle_password
        )

        checkbox.pack(pady=5)

        # ==========================
        # Login Button
        # ==========================

        login_btn = ctk.CTkButton(
            self,
            text="Login",
            width=220,
            height=40,
            command=self.login
        )

        login_btn.pack(pady=20)

        # ==========================
        # Footer
        # ==========================

        footer = ctk.CTkLabel(
            self,
            text="Developed By: Harshada Naik",
            font=("Arial",12)
        )

        footer.pack(side="bottom", pady=15)

    # ==================================

    def toggle_password(self):

        if self.show_password.get():
            self.password.configure(show="")
        else:
            self.password.configure(show="*")

    # ==================================

    def login(self):
         username = self.username.get()
         password = self.password.get()

         if username == "admin" and password == "admin123":
             messagebox.showinfo(
                 "Login",
                 "Login Successful!"
             )

             self.withdraw()

             Dashboard(self)

         else:
             messagebox.showerror(
                 "Login",
                "Invalid Username or Password"
            )
             

        

    