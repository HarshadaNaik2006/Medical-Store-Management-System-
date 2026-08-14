import customtkinter as ctk
from tkinter import messagebox, ttk
from database.db import supplier_collection


class SupplierWindow(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.lift()
        self.focus()
        self.attributes("-topmost", True)
        self.after(100, lambda: self.attributes("-topmost", False))

        self.title("Supplier Management")
        self.geometry("900x700")

        back_btn = ctk.CTkButton(
            self,
            text="← Back to Dashboard",
            width=160,
            command=self.destroy
        )

        back_btn.pack(pady=10)

        title = ctk.CTkLabel(
            self,
            text="Supplier Management",
            font=("Arial", 30, "bold")
        )

        title.pack(pady=20)

        # ==========================
        # Supplier Form
        # ==========================

        form = ctk.CTkFrame(self)
        form.pack(pady=20)

        labels = [
            "Supplier ID",
            "Supplier Name",
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
            text="Save Supplier",
            width=200,
            command=self.save_supplier
        )

        self.save_btn.pack(pady=15)


        self.delete_btn = ctk.CTkButton(
            form,
            text="Delete Supplier",
            width=200,
            fg_color="red",
           command=self.delete_supplier
        )

        self.delete_btn.pack(pady=10)

        self.update_btn = ctk.CTkButton(
            form,
            text="Update Supplier",
            width=200,
            fg_color="green",
            command=self.update_supplier
        )

        self.update_btn.pack(pady=10)

        supplier_list_label = ctk.CTkLabel(
            self,
            text="Supplier List",
            font=("Arial", 22, "bold")
        )

        supplier_list_label.pack(pady=20)

        # ==========================
        # Supplier Search
        # ==========================

        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=5)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=250,
            placeholder_text="Enter Supplier ID"
        )

        self.search_entry.pack(
            side="left",
            padx=5
        )

        self.search_btn = ctk.CTkButton(
            search_frame,
            text="Search Supplier",
            width=150,
            command=self.search_supplier
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
        # Supplier Table
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


        # Table Headings
        self.table.heading(
            "id",
            text="Supplier ID"
        )

        self.table.heading(
            "name",
            text="Supplier Name"
        )

        self.table.heading(
            "phone",
            text="Phone Number"
        )

        self.table.heading(
            "address",
            text="Address"
        )


        # Column Widths
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

        # Scrollbar
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

        # Load supplier data
        self.update_table()

    def save_supplier(self):

        supplier = []

        for entry in self.entries:

            value = entry.get().strip()

            if value == "":
                messagebox.showerror(
                    "Error",
                    "Please fill all fields."
                )
                return

            supplier.append(value)

        supplier_data = {
            "id": supplier[0],
            "name": supplier[1],
            "phone": supplier[2],
            "address": supplier[3]
        }

        existing = supplier_collection.find_one({"id": supplier[0]})

        if existing:
            messagebox.showerror(
                "Error",
                "Supplier ID already exists."
            )
            return

        supplier_collection.insert_one(supplier_data)

        messagebox.showinfo(
            "Success",
            "Supplier Saved Successfully!"
        )

        self.update_table()

        for entry in self.entries:
            entry.delete(0, "end")

    def delete_supplier(self):

        supplier_id = self.entries[0].get().strip()

        if supplier_id == "":
            messagebox.showerror(
                "Error",
                "Enter Supplier ID."
            )
            return

        result = supplier_collection.delete_one(
            {"id": supplier_id}
        )

        if result.deleted_count == 0:
            messagebox.showerror(
                "Error",
                "Supplier not found."
            )
        else:
            messagebox.showinfo(
                "Success",
                "Supplier Deleted Successfully!"
            )

        self.update_table()

        for entry in self.entries:
            entry.delete(0, "end")

    def update_supplier(self):

        supplier = []

        for entry in self.entries:

            value = entry.get().strip()

            if value == "":
                messagebox.showerror(
                    "Error",
                    "Please fill all fields."
                )
                return

            supplier.append(value)

        result = supplier_collection.update_one(
            {"id": supplier[0]},
            {
                "$set": {
                    "name": supplier[1],
                    "phone": supplier[2],
                    "address": supplier[3]
                }
            }
        )

        if result.matched_count == 0:
            messagebox.showerror(
                "Error",
                "Supplier not found."
            )
        else:
            messagebox.showinfo(
                "Success",
                "Supplier Updated Successfully!"
            )

        self.update_table()

        for entry in self.entries:
            entry.delete(0, "end")

    def update_table(self):

        # Clear existing rows
        for item in self.table.get_children():
            self.table.delete(item)

        # Load suppliers from MongoDB
        for supplier in supplier_collection.find():

            self.table.insert(
                "",
                "end",
                values=(
                    supplier.get("id", ""),
                    supplier.get("name", ""),
                    supplier.get("phone", ""),
                    supplier.get("address", "")
                )
            )
    def search_supplier(self):

        supplier_id = self.search_entry.get().strip()

        # ==========================
        # Check Search Text
        # ==========================

        if supplier_id == "":
            messagebox.showerror(
                "Error",
                "Please enter Supplier ID."
            )
            return

        # ==========================
        # Search Supplier
        # ==========================

        supplier = supplier_collection.find_one(
            {"id": supplier_id}
        )

        # ==========================
        # Supplier Not Found
        # ==========================

        if not supplier:

            messagebox.showerror(
                "Error",
                "Supplier ID not found."
            )

            return

        # ==========================
        # Clear Table
        # ==========================

        for item in self.table.get_children():
            self.table.delete(item)

        # ==========================
        # Display Supplier
        # ==========================

        self.table.insert(
            "",
            "end",
            values=(
                supplier.get("id", ""),
                supplier.get("name", ""),
                supplier.get("phone", ""),
                supplier.get("address", "")
            )
        )
        