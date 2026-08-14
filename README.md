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

https://www.python.org/downloads/

After installation, verify that Python is installed:

```bash
python --version
