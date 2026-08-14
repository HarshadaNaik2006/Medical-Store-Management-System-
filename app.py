from flask import Flask, render_template, request, redirect, session
from bson.objectid import ObjectId
from database.web_db import (
    client,
    medicines_collection,
    customers_collection,
    suppliers_collection,
    bills_collection
)

app = Flask(__name__)
app.secret_key = "medical_store_secret_key"
def login_required():

    return session.get("logged_in") is True



@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "admin123":

            session["logged_in"] = True
            session["username"] = username

            return redirect("/")

        else:

            return render_template(
                "login.html",
                error="Invalid username or password."
            )

    return render_template("login.html")

@app.route("/")
def home():

    if not session.get("logged_in"):
        return redirect("/login")

    # Count records
    total_medicines = medicines_collection.count_documents({})
    total_customers = customers_collection.count_documents({})
    total_suppliers = suppliers_collection.count_documents({})
    total_bills = bills_collection.count_documents({})

    # Calculate total sales
    total_sales = 0

    for bill in bills_collection.find():
        total_sales += bill.get("total", 0)

    # Find low-stock medicines
    low_stock_medicines = list(
        medicines_collection.find(
            {"stock": {"$lt": 10}}
        )
    )

    return render_template(
        "dashboard.html",
        total_medicines=total_medicines,
        total_customers=total_customers,
        total_suppliers=total_suppliers,
        total_bills=total_bills,
        total_sales=total_sales,
        low_stock_medicines=low_stock_medicines
    )


@app.route("/medicines")
def medicines():

    if not login_required():
        return redirect("/login")

    search = request.args.get("search", "").strip()

    if search:
        medicines_list = list(
            medicines_collection.find(
                {
                    "name": {
                        "$regex": search,
                        "$options": "i"
                    }
                }
            )
        )
    else:
        medicines_list = list(
            medicines_collection.find()
        )

    return render_template(
        "medicines.html",
        medicines=medicines_list,
        search=search
    )

@app.route("/medicines/add", methods=["GET", "POST"])
def add_medicine():

    if not login_required():
        return redirect("/login")

    if request.method == "POST":

        medicine = {
            "name": request.form["name"],
            "category": request.form["category"],
            "price": float(request.form["price"]),
            "stock": int(request.form["stock"])
        }

        medicines_collection.insert_one(medicine)

        return redirect("/medicines")

    return render_template("add_medicine.html")

@app.route("/medicines/edit/<medicine_id>", methods=["GET", "POST"])
def edit_medicine(medicine_id):
    if not login_required():
        return redirect("/login")

    medicine = medicines_collection.find_one(
        {"_id": ObjectId(medicine_id)}
    )

    if medicine is None:
        return "Medicine not found", 404

    if request.method == "POST":

        updated_medicine = {
            "name": request.form["name"],
            "category": request.form["category"],
            "price": float(request.form["price"]),
            "stock": int(request.form["stock"])
        }

        medicines_collection.update_one(
            {"_id": ObjectId(medicine_id)},
            {"$set": updated_medicine}
        )

        return redirect("/medicines")

    return render_template(
        "edit_medicine.html",
        medicine=medicine
    )

@app.route("/medicines/delete/<medicine_id>")
def delete_medicine(medicine_id):

    if not login_required():
        return redirect("/login")

    medicines_collection.delete_one(
        {"_id": ObjectId(medicine_id)}
    )

    return redirect("/medicines")


@app.route("/customers")
def customers():

    if not login_required():
        return redirect("/login")

    customers_list = list(customers_collection.find())

    return render_template(
        "customers.html",
        customers=customers_list
    )

@app.route("/customers/add", methods=["GET", "POST"])
def add_customer():
    if not login_required():
        return redirect("/login")

    if request.method == "POST":

        customer = {
            "name": request.form["name"],
            "phone": request.form["phone"],
            "email": request.form["email"],
            "address": request.form["address"]
        }

        customers_collection.insert_one(customer)

        return redirect("/customers")

    return render_template("add_customer.html")

@app.route("/customers/edit/<customer_id>", methods=["GET", "POST"])
def edit_customer(customer_id):
    if not login_required():
        return redirect("/login")

    customer = customers_collection.find_one(
        {"_id": ObjectId(customer_id)}
    )

    if customer is None:
        return "Customer not found", 404

    if request.method == "POST":

        updated_customer = {
            "name": request.form["name"],
            "phone": request.form["phone"],
            "email": request.form["email"],
            "address": request.form["address"]
        }

        customers_collection.update_one(
            {"_id": ObjectId(customer_id)},
            {"$set": updated_customer}
        )

        return redirect("/customers")

    return render_template(
        "edit_customer.html",
        customer=customer
    )

@app.route("/customers/delete/<customer_id>")
def delete_customer(customer_id):
    if not login_required():
        return redirect("/login")

    customers_collection.delete_one(
        {"_id": ObjectId(customer_id)}
    )

    return redirect("/customers")

@app.route("/suppliers")
def suppliers():

    if not login_required():
        return redirect("/login")

    suppliers_list = list(suppliers_collection.find())

    return render_template(
        "suppliers.html",
        suppliers=suppliers_list
    )

@app.route("/suppliers/add", methods=["GET", "POST"])
def add_supplier():
    if not login_required():
        return redirect("/login")

    if request.method == "POST":

        supplier = {
            "name": request.form["name"],
            "phone": request.form["phone"],
            "email": request.form["email"],
            "company": request.form["company"],
            "address": request.form["address"]
        }

        suppliers_collection.insert_one(supplier)

        return redirect("/suppliers")

    return render_template("add_supplier.html")

@app.route("/suppliers/edit/<supplier_id>", methods=["GET", "POST"])
def edit_supplier(supplier_id):
    if not login_required():
        return redirect("/login")

    supplier = suppliers_collection.find_one(
        {"_id": ObjectId(supplier_id)}
    )

    if supplier is None:
        return "Supplier not found", 404

    if request.method == "POST":

        updated_supplier = {
            "name": request.form["name"],
            "phone": request.form["phone"],
            "email": request.form["email"],
            "company": request.form["company"],
            "address": request.form["address"]
        }

        suppliers_collection.update_one(
            {"_id": ObjectId(supplier_id)},
            {"$set": updated_supplier}
        )

        return redirect("/suppliers")

    return render_template(
        "edit_supplier.html",
        supplier=supplier
    )

@app.route("/suppliers/delete/<supplier_id>")
def delete_supplier(supplier_id):
    if not login_required():
        return redirect("/login")

    suppliers_collection.delete_one(
        {"_id": ObjectId(supplier_id)}
    )

    return redirect("/suppliers")

@app.route("/bills")
def bills():

    if not login_required():
        return redirect("/login")

    bills_list = list(
        bills_collection.find().sort("_id", -1)
    )

    return render_template(
        "bills.html",
        bills=bills_list
    )

@app.route("/bills/add", methods=["GET", "POST"])
def add_bill():

    if not login_required():
        return redirect("/login")

    if request.method == "POST":

        customer_id = request.form["customer_id"]
        medicine_id = request.form["medicine_id"]
        quantity = int(request.form["quantity"])

        # Find customer
        customer = customers_collection.find_one(
            {"_id": ObjectId(customer_id)}
        )

        # Find medicine
        medicine = medicines_collection.find_one(
            {"_id": ObjectId(medicine_id)}
        )

        if customer is None or medicine is None:
            return "Customer or medicine not found", 404

        # Check available stock
        current_stock = medicine.get("stock", 0)

        if quantity > current_stock:
            return (
                f"Not enough stock available. "
                f"Only {current_stock} units are available.",
                400
            )

        # Calculate total
        total = medicine["price"] * quantity

        # Reduce medicine stock
        medicines_collection.update_one(
            {"_id": medicine["_id"]},
            {"$inc": {"stock": -quantity}}
        )

        # Create bill
        bill = {
            "customer_id": customer["_id"],
            "customer_name": customer["name"],
            "medicine_id": medicine["_id"],
            "medicine_name": medicine["name"],
            "quantity": quantity,
            "price": medicine["price"],
            "total": total,
            "date": __import__("datetime").datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        bills_collection.insert_one(bill)

        return redirect("/bills")

    customers_list = list(
        customers_collection.find()
    )

    medicines_list = list(
        medicines_collection.find()
    )

    return render_template(
        "add_bill.html",
        customers=customers_list,
        medicines=medicines_list
    )

@app.route("/bills/view/<bill_id>")
def view_bill(bill_id):

    if not login_required():
        return redirect("/login")

    bill = bills_collection.find_one(
        {"_id": ObjectId(bill_id)}
    )

    if bill is None:
        return "Bill not found", 404

    return render_template(
        "invoice.html",
        bill=bill
    )

@app.route("/bills/delete/<bill_id>")
def delete_bill(bill_id):
    if not login_required():
        return redirect("/login")

    bills_collection.delete_one(
        {"_id": ObjectId(bill_id)}
    )

    return redirect("/bills")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")

if __name__ == "__main__":

    try:
        client.admin.command("ping")
        print("MongoDB connection successful!")

    except Exception as e:
        print("MongoDB connection failed:", e)

    app.run(debug=True)