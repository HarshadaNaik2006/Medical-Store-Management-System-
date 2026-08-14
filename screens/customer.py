import customtkinter as ctk
from tkinter import Text, messagebox,ttk
from database.db import customer_collection

class CustomerWindow(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)
        self.lift()
        self.focus()
        self.attributes("-topmost", True)
        self.after(100, lambda: self.attributes("-topmost", False))
        

        self.title("Customer Management")
        self.geometry("900x700")

        back_btn = ctk.CTkButton(
            self,
            text="← Back to Dashboard",
            width=180,
            command=self.destroy
        )

        back_btn.pack(pady=10)

        self.customer_list = []

        title = ctk.CTkLabel(
            self,
            text="Customer Management",
            font=("Arial", 30, "bold")
        )

        title.pack(pady=20)

        # ==========================
        # Customer Form
        # ==========================

        form = ctk.CTkFrame(self)
        form.pack(pady=20)

        labels = [
            "Customer ID",
            "Customer Name",
            "Phone Number",
            "Address"
        ]

        self.entries = []

        for label in labels:

            ctk.CTkLabel(
            form,
            text=label,
            font=("Arial", 15)
            ).pack(pady=5)

            entry = ctk.CTkEntry(
                form,
                width=300
            )

            entry.pack(pady=5)

            self.entries.append(entry)

        self.save_btn = ctk.CTkButton(
            form,
            text="Save Customer",
            width=200,
            command=self.save_customer
        )

        self.save_btn.pack(pady=15)
        
        self.delete_btn = ctk.CTkButton(
            form,
            text="Delete Customer",
            width=200,
            fg_color="red",
            command=self.delete_customer
        )

        self.delete_btn.pack(pady=10)

        self.update_btn = ctk.CTkButton(
            form,
            text="Update Customer",
            width=200,
            fg_color="green",
            command=self.update_customer
        )

        self.update_btn.pack(pady=10)

        customer_list_label = ctk.CTkLabel(
            self,
            text="Customer List",
            font=("Arial", 22, "bold")
        )

        customer_list_label.pack(pady=20)

        # ==========================
        # Customer Search
        # ==========================

        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=5)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=250,
            placeholder_text="Enter Customer ID"
        )

        self.search_entry.pack(
            side="left",
            padx=5
        )

        self.search_btn = ctk.CTkButton(
            search_frame,
            text="Search Customer",
            width=150,
            command=self.search_customer
        )

        self.search_btn.pack(
            side="left",
            padx=5
        )

        self.show_all_btn = ctk.CTkButton(
            search_frame,
            text="Show All",
            width=100,
            command=self.update_table
        )

        self.show_all_btn.pack(
            side="left",
            padx=5
        )

        # ==========================
        # Customer Table
        # ==========================

        table_frame = ctk.CTkFrame(self)
        table_frame.pack(
            padx=30,
            pady=10,
            fill="both",
            expand=True
        )

        columns = (
            "id",
            "name",
            "phone",
            "address"
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10
        )

        self.table.heading(
            "id",
            text="Customer ID"
        )

        self.table.heading(
            "name",
            text="Customer Name"
        )

        self.table.heading(
            "phone",
            text="Phone Number"
        )

        self.table.heading(
            "address",
            text="Address"
        )

        self.table.column(
            "id",
            width=120,
            anchor="center"
        )

        self.table.column(
            "name",
            width=220,
            anchor="center"
        )

        self.table.column(
            "phone",
            width=180,
            anchor="center"
        )

        self.table.column(
            "address",
            width=250,
            anchor="center"
        )

        self.table.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.table.configure(
            yscrollcommand=scrollbar.set
        )

        self.update_table()

    def save_customer(self):

        customer = []

        for entry in self.entries:

            value = entry.get().strip()

            if value == "":
                messagebox.showerror(
                    "Error",
                    "Please fill all fields."
                )
                return

            customer.append(value)

        customer_data = {
            "id": customer[0],
            "name": customer[1],
            "phone": customer[2],
            "address": customer[3]
        }

        existing = customer_collection.find_one({"id": customer[0]})

        if existing:
            messagebox.showerror(
                "Error",
                "Customer ID already exists."
            )
            return

        customer_collection.insert_one(customer_data)

        messagebox.showinfo(
            "Success",
            "Customer Saved Successfully!"
        )
        self.update_table()

        for entry in self.entries:
            entry.delete(0, "end")

    def update_table(self):

        # Clear existing rows
        for item in self.table.get_children():
            self.table.delete(item)

        # Load customers from MongoDB
        for customer in customer_collection.find():

            self.table.insert(
                "",
                "end",
                values=(
                    customer.get("id", ""),
                    customer.get("name", ""),
                    customer.get("phone", ""),
                    customer.get("address", "")
                )
            )
    def delete_customer(self):

        customer_id = self.entries[0].get().strip()

        if customer_id == "":
            messagebox.showerror(
                "Error",
                "Please enter Customer ID."
            )
            return

        result = customer_collection.delete_one({"id": customer_id})

        if result.deleted_count == 0:
            messagebox.showerror(
                "Error",
                "Customer ID not found."
            )
            return

        messagebox.showinfo(
            "Success",
            "Customer Deleted Successfully!"
        )

        self.update_table()

        for entry in self.entries:
            entry.delete(0, "end")  

    def update_customer(self):

        customer = []

        for entry in self.entries:

            value = entry.get().strip()

            if value == "":
                messagebox.showerror(
                    "Error",
                    "Please fill all fields."
                )
                return

            customer.append(value)

        existing = customer_collection.find_one({"id": customer[0]})

        if not existing:
            messagebox.showerror(
                "Error",
                "Customer ID not found."
            )
            return

        customer_collection.update_one(
            {"id": customer[0]},
            {
                "$set": {
                    "name": customer[1],
                    "phone": customer[2],
                    "address": customer[3]
                }
            }
        )

        messagebox.showinfo(
            "Success",
            "Customer Updated Successfully!"
        )

        self.update_table()

        for entry in self.entries:
            entry.delete(0, "end")  

    def search_customer(self):

        customer_id = self.search_entry.get().strip()

        if customer_id == "":
            messagebox.showerror(
                "Error",
                "Please enter Customer ID."
            )
            return

        customer = customer_collection.find_one(
            {"id": customer_id}
        )

        if not customer:

            messagebox.showerror(
                "Error",
                "Customer ID not found."
            )

            return

        # Clear table
        for item in self.table.get_children():
            self.table.delete(item)

        # Display searched customer
        self.table.insert(
            "",
            "end",
            values=(
                customer.get("id", ""),
                customer.get("name", ""),
                customer.get("phone", ""),
                customer.get("address", "")
            )
        )