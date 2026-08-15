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

```
## Setup and Installation

Follow the steps below to run the Medical Store Management System on your computer.

### 1. Install Python

Download and install Python 3 from:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

After installation, verify that Python is installed:

```bash
python --version
```

You should see your installed Python version.

### 2. Install MongoDB

Download and install **MongoDB Community Server** from:

[https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)

Make sure the MongoDB server is running before starting the application.

### 3. Clone the GitHub Repository

Open **Command Prompt** or **PowerShell** and run:

```bash
https://github.com/HarshadaNaik2006/Medical-Store-Management-System-.git
```

Then open the project folder:

```bash
cd MedicalStoreManagement
```

### 4. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv env
```

This will create an `env` folder inside the project.

The `env` folder is ignored by Git using `.gitignore`.

### 5. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.\env\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
env\Scripts\activate
```

After successful activation, you should see:

```text
(env)
```

at the beginning of your terminal.

### 6. Install Required Packages

Install Flask and PyMongo:

```bash
pip install flask pymongo
```

The project uses:

- **Flask** - Web application framework
- **PyMongo** - Python library for connecting to MongoDB

### 7. Start MongoDB

Make sure MongoDB is running before starting the Flask application.

MongoDB is used to store:

- Medicines
- Customers
- Suppliers
- Bills
- Inventory information

### 8. Run the Flask Application

Inside the project folder, run:

```bash
python app.py
```

If everything is configured correctly, the terminal will display something similar to:

```text
Serving Flask app 'app'
Debug mode: on
Running on http://127.0.0.1:5000
```

### 9. Open the Application

Open your web browser and visit:

```text
http://127.0.0.1:5000
```

The **Medical Store Management System** login page will appear.

### 10. Login Credentials

For demonstration purposes, use:

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `admin123` |

After successful login, the user will be redirected to the dashboard.

If a user tries to access protected pages without logging in, the system redirects the user to the login page.

## Important Notes

- Make sure MongoDB is running before starting the Flask application.
- The `env` folder is ignored by Git and does not need to be uploaded to GitHub.
- If the `env` folder does not exist after cloning the repository, create it again using:

```bash
python -m venv env
```

- Activate the virtual environment before installing packages.
- Install the required packages using:

```bash
pip install flask pymongo
```

- Run the application using:

```bash
python app.py
```

## .gitignore

Since the project only needs to ignore the `env` folder, your `.gitignore` file should contain:

```gitignore
env/
```

Project Demo Video
[▶️ Watch the Medical Store Management System Demo]=https://youtu.be/XmWVPE6UJMw
