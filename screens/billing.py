import customtkinter as ctk
from tkinter import Text, messagebox
from database.db import customer_collection, medicine_collection, bill_collection


class BillingWindow(ctk.CTkToplevel):

    def __init__(self, parent):

        super().__init__(parent)

        self.lift()
        self.focus()
        self.attributes("-topmost", True)
        self.after(100, lambda: self.attributes("-topmost", False))

        self.title("Billing Management")
        self.geometry("900x700")

        back_btn = ctk.CTkButton(

            self,
            text="← Back to Dashboard",
            width=180,
            command=self.destroy
        )
        
        back_btn.pack(pady=10)

        title = ctk.CTkLabel(
            self,
            text="Billing Management",
            font=("Arial", 30, "bold")
        )

        title.pack(pady=20)

        # ==========================
        # Billing Form
        # ==========================

        form = ctk.CTkFrame(self)
        form.pack(pady=20)

        labels = [
            "Bill ID",
            "Customer ID",
            "Medicine Name",
            "Quantity",
            "Price"
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
        # Generate Bill Button
        # ==========================

        self.bill_btn = ctk.CTkButton(
            form,
            text="Generate Bill",
            width=200,
            command=self.generate_bill
        )

        self.bill_btn.pack(pady=15)

        # ==========================
        # Bill Display
        # ==========================

        bill_label = ctk.CTkLabel(
            self,
            text="Bill Details",
            font=("Arial", 22, "bold")
        )

        bill_label.pack(pady=20)

        self.bill_table = Text(
            self,
            width=90,
            height=12,
            font=("Arial", 11)
        )

        self.bill_table.pack(pady=10)

    # ==========================
    # Generate Bill
    # ==========================

    def generate_bill(self):

        values = []

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

            values.append(value)

        bill_id = values[0]
        customer_id = values[1]
        medicine_name = values[2]
        quantity_text = values[3]
        entered_price = values[4]

        # ==========================
        # Check Duplicate Bill ID
        # ==========================

        existing_bill = bill_collection.find_one(
            {"bill_id": bill_id}
        )

        if existing_bill:
            messagebox.showerror(
                "Error",
                "Bill ID already exists. Please use a different Bill ID."
            )
            return

        # ==========================
        # Convert quantity
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
        # Check Customer
        # ==========================

        existing_customer = customer_collection.find_one(
            {"id": customer_id}
        )

        if not existing_customer:

            messagebox.showerror(
                "Error",
                "Customer ID does not exist."
            )

            return

        # ==========================
        # Check Medicine
        # ==========================

        existing_medicine = medicine_collection.find_one(
            {"name": medicine_name}
        )

        if not existing_medicine:

            messagebox.showerror(
                "Error",
                "Medicine does not exist."
            )

            return

        # ==================================
        # Get Available Stock from database
        # ================================

        try:

            available_quantity = int(
                existing_medicine.get("quantity", 0)
            )

        except (ValueError, TypeError):
            messagebox.showerror(
                "Error",
                "Medicine quantity in database is invalid."
            )
            return

        # ==========================
        # Check Stock
        # ==========================

        if quantity > available_quantity:

            messagebox.showerror(
                "Error",
                f"Insufficient stock. Available quantity: {available_quantity}"
            )

            return

        # ==========================
        # Get Medicine Price
        # ==========================

        medicine_price = existing_medicine.get("price", "")

        try:

            price = float(
                str(medicine_price)
                .replace("₹", "")
                .strip()
            )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Invalid medicine price in database."
            )

            return

        # ==========================
        # Calculate Total
        # ==========================

        total = quantity * price


        # ==========================
        # Reduce Medicine Stock
        # ==========================

        stock_result = medicine_collection.update_one(
            {
                "_id": existing_medicine["_id"],
                "quantity": {"$gte": quantity}
            },
            {
                "$inc": {
                    "quantity": -quantity
                }
            }
        )

        # Check if stock was successfully reduced

        if stock_result.modified_count == 0:

            messagebox.showerror(
                "Error",
                "Stock could not be updated. Please try again."
            )

            return


        # ==========================
        # Save Bill
        # ==========================

        bill_data = {
            "bill_id": bill_id,
            "customer_id": customer_id,
            "medicine_name": medicine_name,
            "quantity": quantity,
            "price": price,
            "total": total
        }

        bill_collection.insert_one(bill_data)

        # ==========================
        # Display Bill
        # ==========================

        self.bill_table.delete("1.0", "end")

        self.bill_table.insert(
            "end",
            "============================== BILL ==============================\n"
        )

        self.bill_table.insert(
            "end",
            f"Bill ID       : {bill_id}\n"
        )

        self.bill_table.insert(
            "end",
            f"Customer ID   : {customer_id}\n"
        )

        self.bill_table.insert(
            "end",
            f"Medicine      : {medicine_name}\n"
        )

        self.bill_table.insert(
            "end",
            f"Quantity      : {quantity}\n"
        )

        self.bill_table.insert(
            "end",
            f"Price         : ₹{price:.2f}\n"
        )

        self.bill_table.insert(
            "end",
            f"Total Amount  : ₹{total:.2f}\n"
        )

        self.bill_table.insert(
            "end",
            "====================================================================\n"
        )

        messagebox.showinfo(
            "Success",
            "Bill Generated Successfully!"
        )   