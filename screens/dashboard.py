import customtkinter as ctk
from screens.medicine import MedicineWindow
from screens.customer import CustomerWindow
from screens.supplier import SupplierWindow
from screens.billing import BillingWindow

class Dashboard:

    def __init__(self,parent):

        self.window = ctk.CTkToplevel(parent)

        self.window.title("Medical Store Dashboard")

        self.window.geometry("1100x650")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # ==========================
        # Heading
        # ==========================

        title = ctk.CTkLabel(
            self.window,
            text="🏥 Medical Store Management System",
            font=("Arial", 30, "bold")
        )

        title.pack(pady=20)

        subtitle = ctk.CTkLabel(
            self.window,
            text="Dashboard",
            font=("Arial", 20)
        )

        subtitle.pack(pady=5)

        # ==========================
        # Buttons
        # ==========================
        self.medicine_btn = ctk.CTkButton(
            self.window,
            text="💊 Medicine Management",
            width=300,
            height=45,
            command=self.open_medicine
        )

        self.medicine_btn.pack(pady=10)

        self.customer_btn = ctk.CTkButton(
            self.window,
            text="👤 Customer Management",
            width=300,
            height=45,
            command=self.open_customer
        )

        self.customer_btn.pack(pady=10)

        self.supplier_btn = ctk.CTkButton(
            self.window,
            text="🚚 Supplier Management",
            width=300,
            height=45,
            command=self.open_supplier
        )

        self.supplier_btn.pack(pady=10)

        self.billing_btn = ctk.CTkButton(
            self.window,
            text="🧾 Billing System",
            width=300,
            height=45,
            command=self.open_billing
        )

        self.billing_btn.pack(pady=10)

        self.logout_btn = ctk.CTkButton(
            self.window,
            text="Logout",
            fg_color="red",
            width=300,
            height=45,
            command=self.window.destroy
        )

        self.logout_btn.pack(pady=30)

        #self.window.mainloop()

    def open_medicine(self):
        MedicineWindow(self.window)

    def open_customer(self):
        CustomerWindow(self.window)

    def open_supplier(self):
        SupplierWindow(self.window)

    def open_billing(self):
        BillingWindow(self.window)         
             

       