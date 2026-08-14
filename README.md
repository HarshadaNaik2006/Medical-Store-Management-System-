# Medical Store Management System

A web-based Medical Store Management System developed using Python Flask, HTML, CSS, JavaScript, and MongoDB. The project helps manage medicines, customers, suppliers, inventory, and billing operations.

## Features

- Admin Login and Logout
- Dashboard
- Medicine Management
  - Add medicines
  - View medicines
  - Update medicines
  - Delete medicines
  - Search medicines
- Customer Management
  - Add customers
  - View customers
  - Update customers
  - Delete customers
- Supplier Management
  - Add suppliers
  - View suppliers
  - Update suppliers
  - Delete suppliers
- Billing Management
- Automatic bill calculation
- Automatic stock reduction after billing
- Stock availability validation
- Low-stock monitoring
- Printable invoices
- PDF invoice generation
- MongoDB database integration

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Database
- MongoDB
- PyMongo

## Project Structure

```text
MedicalStoreManagement/
│
├── app.py
├── customer.py
├── supplier.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── medicines.html
│   ├── add_medicine.html
│   ├── customers.html
│   ├── suppliers.html
│   ├── bills.html
│   ├── add_bill.html
│   └── invoice.html
│
├── static/
│   └── css/
│       └── style.css
│
└── README.md

Setup and Installation

Follow the steps below to run the project on your computer.

1. Install Python

Download and install Python 3 from:

https://www.python.org/downloads/

After installation, verify Python:

python --version

You should see your installed Python version.

2. Install MongoDB

Download and install MongoDB Community Server from:

https://www.mongodb.com/try/download/community

After installation, make sure the MongoDB server is running.

MongoDB is used as the backend database for this project.

3. Clone the GitHub Repository

Open Command Prompt or PowerShell and run:

git clone YOUR_GITHUB_REPOSITORY_LINK

Then open the project folder:

cd MedicalStoreManagement
4. Create a Virtual Environment

Create a Python virtual environment:

python -m venv venv

A folder named venv will be created inside the project.

5. Activate the Virtual Environment
Windows PowerShell
.\venv\Scripts\Activate.ps1
Windows Command Prompt
venv\Scripts\activate

After activation, the terminal should show:

(venv)
6. Install Required Python Packages

Install Flask and PyMongo:

pip install flask pymongo

The project uses:

Flask for the web application
PyMongo for connecting Python with MongoDB
7. Start MongoDB

Make sure MongoDB is running before starting the Flask application.

The application requires MongoDB because all medicines, customers, suppliers, and bills are stored in the MongoDB database.

8. Run the Flask Application

Inside the project folder, run:

python app.py

If everything is configured correctly, the terminal will display something similar to:

Serving Flask app 'app'
Debug mode: on
Running on http://127.0.0.1:5000
9. Open the Application

Open a web browser and visit:

http://127.0.0.1:5000

The Medical Store Management System login page will appear.

Login Credentials

For demonstration purposes, use:

Username: admin
Password: admin123

After successful login, the user will be redirected to the dashboard.

If a user tries to access protected pages without logging in, the system redirects the user to the login page.
