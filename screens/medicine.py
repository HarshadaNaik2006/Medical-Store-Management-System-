import customtkinter as ctk
from tkinter import messagebox,ttk
from database.db import medicine_collection


class MedicineWindow(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.lift()
        self.focus()
        

        self.attributes("-topmost",True)
        self.after(100,lambda: self.attributes("-topmost",False))

        self.title("Medicine Management")
        self.geometry("1000x800")

        back_btn = ctk.CTkButton(
        self,
        text="← Back to Dashboard",
        command=self.destroy,
        width=160
        )

        back_btn.pack(pady=10)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # ==========================
        # Title
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="Medicine Management",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        # ==========================
        # Form
        # ==========================

        form = ctk.CTkFrame(self)
        form.pack(pady=20)

        labels = [
            "Medicine ID",
            "Medicine Name",
            "Company",
            "Price",
            "Quantity",
            "Expiry Date"
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

        # ==========================
        # Save Button
        # ==========================

        save_btn = ctk.CTkButton(
            form,
            text="Save Medicine",
            width=200,
            command=self.save_medicine
        )

        save_btn.pack(pady=20)
        
        delete_btn = ctk.CTkButton(
              form,
              text="Delete Medicine",
              width=200,
              fg_color="red",
              command=self.delete_medicine
        )

        delete_btn.pack(pady=10)

        update_btn = ctk.CTkButton(
            form,
            text="Update Medicine",
            fg_color="green",
            command=self.update_medicine
        )

        update_btn.pack(pady=10)
        # ==========================
        # Search Medicine
        # ==========================

        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=10)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=250,
            placeholder_text="Enter Medicine ID or Name"
        )

        self.search_entry.pack(
            side="left",
            padx=5
        )

        search_btn = ctk.CTkButton(
            search_frame,
            text="Search Medicine",
            width=150,
            command=self.search_medicine
        )

        search_btn.pack(
            side="left",
            padx=5
        )

        show_all_btn = ctk.CTkButton(
            search_frame,
            text="Show All",
            width=100,
            command=self.update_table
        )

        show_all_btn.pack(
            side="left",
            padx=5
        )
        # ==========================
        # Medicine Table
        # ==========================

        table_title = ctk.CTkLabel(
            self,
            text="Medicine List",
            font=("Arial", 22, "bold")
        )

        table_title.pack(pady=10)

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
            "company",
            "price",
            "quantity",
            "expiry"
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10
        )

        # Column headings

        self.table.heading(
            "id",
            text="Medicine ID"
        )

        self.table.heading(
            "name",
            text="Medicine Name"
        )

        self.table.heading(
            "company",
            text="Company"
        )

        self.table.heading(
            "price",
            text="Price"
        )

        self.table.heading(
            "quantity",
            text="Quantity"
        )

        self.table.heading(
            "expiry",
            text="Expiry Date"
        )

        # Column widths

        self.table.column(
            "id",
            width=120,
            anchor="center"
        )

        self.table.column(
            "name",
            width=250,
            anchor="center"
        )

        self.table.column(
            "company",
            width=180,
            anchor="center"
        )

        self.table.column(
            "price",
            width=100,
            anchor="center"
        )

        self.table.column(
            "quantity",
            width=100,
            anchor="center"
        )

        self.table.column(
            "expiry",
            width=150,
            anchor="center"
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

        self.table.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.update_table()


    # ==========================
    # Save Medicine
    # ==========================

    def save_medicine(self):

        medicine = []

        # ==========================
        # Get form values
        # ==========================

        for entry in self.entries:

            value = entry.get().strip()

            if value == "":
                messagebox.showerror(
                    "Error",
                    "Please fill all fields."
                )
                return

            medicine.append(value)

        medicine_id = medicine[0]
        medicine_name = medicine[1]
        company = medicine[2]
        price_text = medicine[3]
        quantity_text = medicine[4]
        expiry = medicine[5]

        # ==========================
        # Check Duplicate Medicine ID
        # ==========================

        existing = medicine_collection.find_one(
            {"id": medicine_id}
        )   

        if existing:

            messagebox.showerror(
                "Error",
                "Medicine ID already exists."
            )

            return

        # ==========================
        # Validate Price
        # ==========================

        try:

            price = float(
                price_text.replace("₹", "").strip()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Price must be a valid number."
            )

            return

        if price <= 0:

            messagebox.showerror(
                "Error",
                "Price must be greater than 0."
            )

            return

        # ==========================
        # Validate Quantity
        # ==========================

        try:

            quantity = int(quantity_text)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Quantity must be a whole number."
            )

            return

        if quantity <= 0:

            messagebox.showerror(
                "Error",
                "Quantity must be greater than 0."
            )

            return

        # ==========================
        # Create Medicine Data
        # ==========================

        medicine_data = {

            "id": medicine_id,

            "name": medicine_name,

            "company": company,

            "price": price,

            "quantity": quantity,

            "expiry": expiry
        }

        # ==========================
        # Save to MongoDB
        # ==========================

        medicine_collection.insert_one(
            medicine_data
        )

        messagebox.showinfo(
            "Success",
            "Medicine Saved Successfully!"
        )

        # Refresh table

        self.update_table()

        # Clear fields

        for entry in self.entries:

            entry.delete(0, "end")

    # ==========================
    # Update Table
    # ==========================

    def update_table(self):

        # Clear existing Treeview rows
        for item in self.table.get_children():
            self.table.delete(item)

        # Load medicines from MongoDB
        for medicine in medicine_collection.find():

            self.table.insert(
                "",
                "end",
                values=(
                    medicine.get("id", ""),
                    medicine.get("name", ""),
                    medicine.get("company", ""),
                    medicine.get("price", ""),
                    medicine.get("quantity", ""),
                    medicine.get("expiry", "")
                )
            )
        
        
    def delete_medicine(self):

        medicine_id = self.entries[0].get().strip()

        # ==========================
        # Check Medicine ID
        # ==========================

        if medicine_id == "":
            messagebox.showerror(
                "Error",
                "Please enter Medicine ID."
            )
            return

        # ==========================
        # Find Medicine
        # ==========================

        existing_medicine = medicine_collection.find_one(
            {"id": medicine_id}
        )

        if not existing_medicine:
            messagebox.showerror(
                "Error",
                "Medicine ID not found."
            )
            return

        # ==========================
        # Confirm Delete
        # ==========================

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete\n"
            f"{existing_medicine.get('name', '')}?"
        )

        if not confirm:
            return

        # ==========================
        # Delete Medicine
        # ==========================

        medicine_collection.delete_one(
            {"id": medicine_id}
        )

        messagebox.showinfo(
            "Success",
            "Medicine Deleted Successfully!"
        )

        # ==========================
        # Refresh Table
        # ==========================

        self.update_table()

        # ==========================
        # Clear Fields
        # ==========================

        for entry in self.entries:
            entry.delete(0, "end")

    #update medicine

    def update_medicine(self):

        medicine = []

        # Get Form Values
        for entry in self.entries:

            value = entry.get().strip()

            if value == "":
                messagebox.showerror(
                    "Error",
                    "Please fill all fields."
                )
                return

            medicine.append(value)

        medicine_id = medicine[0]
        medicine_name = medicine[1]
        company = medicine[2]
        price_text = medicine[3]
        quantity_text = medicine[4]
        expiry = medicine[5]

    
        # Check Medicine ID
    
        existing_medicine = medicine_collection.find_one(
            {"id": medicine_id}
        )

        if not existing_medicine:

            messagebox.showerror(
                "Error",
                "Medicine ID not found."
            )

            return

   
        # Validate Price
        try:

            price = float(
                price_text.replace("₹", "").strip()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Price must be a valid number."
            )

            return

        if price <= 0:

            messagebox.showerror(
                "Error",
                "Price must be greater than 0."
            )

            return

    
        # Validate Quantity
        try:

            quantity = int(quantity_text)

        except ValueError:

            messagebox.showerror(
                "Error",
                "Quantity must be a whole number."
            )

            return

        if quantity <= 0:

            messagebox.showerror(
                "Error",
                "Quantity must be greater than 0."
            )

            return

    
        # Update Medicine
    

        medicine_collection.update_one(

            {"id": medicine_id},

            {
                "$set": {
                    "name": medicine_name,
                    "company": company,
                    "price": price,
                    "quantity": quantity,
                    "expiry": expiry
                }
            }
        )

    
        # Success Message
        messagebox.showinfo(
            "Success",
            "Medicine Updated Successfully!"
        )

        # Refresh Table
        self.update_table()

        # Clear Fields
        for entry in self.entries:
            entry.delete(0, "end")

    def search_medicine(self):

        search_text = self.search_entry.get().strip()

        # ==========================
        # Check Search Text
        # ==========================

        if search_text == "":
            messagebox.showerror(
                "Error",
                "Please enter Medicine ID or Name."
            )
            return

        # ==========================
        # Search Medicine
        # ==========================

        medicine = medicine_collection.find_one(
            {
                "$or": [
                    {"id": search_text},
                    {"name": search_text}
                ]
            }   
        )

        # ==========================
        # Medicine Not Found
        # ==========================

        if not medicine:
            messagebox.showerror(
                "Error",
                "Medicine not found."
            )
            return

        # ==========================
        # Clear Treeview
        # ==========================

        for item in self.table.get_children():
            self.table.delete(item)

        # ==========================
        # Display Medicine
        # ==========================

        self.table.insert(
            "",
            "end",
            values=(
                medicine.get("id", ""),
                medicine.get("name", ""),
                medicine.get("company", ""),
                medicine.get("price", ""),
                medicine.get("quantity", ""),
                medicine.get("expiry", "")
            )
        ) 