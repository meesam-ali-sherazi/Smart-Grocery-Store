
# 🛒 Smart Grocery Store Management System

> A simple Python-based application to manage grocery products, inventory, customer sales, and store reports efficiently.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Project](https://img.shields.io/badge/Project-Management-orange)
![Type](https://img.shields.io/badge/Type-CLI%20Application-green)
![Tests](https://img.shields.io/badge/Testing-11%20Cases-brightgreen)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Project Description

The **Smart Grocery Store Management System** is a menu-driven application developed using Python.

It helps a local grocery store manage product details, prices, available stock, and customer sales.

The system allows the store owner to add new products, view all products, search for products, update stock quantities, process customer purchases, view sales records, and generate a complete store report.

This project uses Python concepts such as variables, lists, dictionaries, functions, loops, conditional statements, and exception handling.

---

## 📑 Table of Contents

1. [Project Features](#-project-features)
2. [Technologies Used](#-technologies-used)
3. [Project Structure](#-project-structure)
4. [How to Run the Project](#-how-to-run-the-project)
5. [Application Menu](#-application-menu)
6. [Validation Rules](#-validation-rules)
7. [Testing](#-testing)
8. [Edge-Case Test Results](#-edge-case-test-results)
9. [Expected Output](#-expected-output)
10. [Future Improvements](#-future-improvements)

---

## ✨ Project Features

The system provides the following features:

### 1. Product Management
- Add new grocery products.
- Assign a unique Product ID.
- Store product name, category, price, and stock.
- Prevent duplicate Product IDs.

### 2. View Products
- Display all available products.
- Show Product ID, name, category, price, and stock.

### 3. Search Products
- Search products by name.
- Search products by Product ID.
- Display complete product information.

### 4. Update Stock
- Add more stock to existing products.
- Set a new stock quantity.
- Prevent negative stock values.

### 5. Process Customer Sales
- Select products using Product ID.
- Enter purchase quantity.
- Check available stock.
- Calculate total bill.
- Automatically deduct sold quantity from inventory.

### 6. Sales Records
- Store completed sales.
- Display product name and ID.
- Show quantity sold and total amount.

### 7. Store Report
- Calculate total number of products.
- Calculate total available stock.
- Display total sales transactions.
- Calculate total revenue.
- Identify products with stock below 5.
- Find the highest-priced product.
- Find the lowest-priced product.

---

## 🛠 Technologies Used

- **Programming Language:** Python
- **Data Structures:** Lists and Dictionaries
- **Concepts:** Functions, Loops, Conditions, Exception Handling
- **Library:** math
- **Testing Framework:** unittest
- **Code Editor:** Visual Studio Code

---

## 📂 Project Structure

```text
smart_grocery_store/
│
├── smart_grocery_store.py
│
└── README.md
```

**File Description:**

- `smart_grocery_store.py` - Main application containing all grocery store functions.
- `test_smart_grocery_store.py` - Automated tests for checking edge cases.
- `README.md` - Project documentation and instructions.

---

## ▶ How to Run the Project

### Step 1: Install Python

Install Python 3.8 or newer.

### Step 2: Open Project Folder

Open the project folder in Visual Studio Code.

### Step 3: Open Terminal

Open the VS Code terminal.

### Step 4: Run the Program

```bash
python smart_grocery_store.py
```

On some systems, use:

```bash
python3 smart_grocery_store.py
```

### Step 5: Use the Application

Select an option from the main menu and follow the instructions.

---

## 📋 Application Menu

The application provides the following menu:

| Option | Function |
|---|---|
| 1 | Add New Product |
| 2 | View All Products |
| 3 | Search Product |
| 4 | Update Product Stock |
| 5 | Process Customer Sale |
| 6 | View Sales Records |
| 7 | Generate Store Report |
| 8 | Exit |

---

## 🔒 Validation Rules

The system includes input validation to prevent incorrect data.

- Product ID must be a positive integer.
- Product ID must be unique.
- Product name cannot be empty.
- Product category cannot be empty.
- Price must be greater than zero.
- Price must be a finite number.
- Stock cannot be negative.
- Purchase quantity must be greater than zero.
- Purchase quantity cannot exceed available stock.
- Invalid numeric inputs are handled using `try-except`.

---

## 🧪 Testing

The project includes executable edge-case tests using Python's built-in `unittest` framework.

To execute the tests, run:

```bash
python -m unittest -v
```

The test file checks different situations to make sure the application works correctly.

---

## 📊 Edge-Case Test Results

The following 11 test cases were executed successfully.

| No. | Test Case | Expected Result | Status |
|---|---|---|---|
| 1 | Zero Product ID | Reject input | PASS |
| 2 | Negative Product ID | Reject input | PASS |
| 3 | Duplicate Product ID | Reject duplicate | PASS |
| 4 | Infinite Price | Reject price | PASS |
| 5 | NaN Price | Reject price | PASS |
| 6 | Zero Price | Reject price | PASS |
| 7 | Negative Stock | Reject stock | PASS |
| 8 | Insufficient Stock | Reject sale | PASS |
| 9 | Zero Purchase Quantity | Reject sale | PASS |
| 10 | Successful Sale | Update stock and record sale | PASS |
| 11 | Invalid Numeric Input | Display error message | PASS |

### Test Summary

- Total Test Cases: 11
- Passed: 11
- Failed: 0

**Overall Result: All 11 tests passed.**

These results are from the recorded test execution. Run the test command again to verify the current version of the code.

---

## 💻 Expected Output

```text
====================================
     SMART GROCERY STORE SYSTEM
====================================
1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit

Enter your choice:
```

---

## 🚀 Future Improvements

The project can be improved in the future by adding:

- Database connectivity.
- Graphical User Interface (GUI).
- Customer management.
- Printable sales receipts.
- Daily and monthly sales reports.
- User login and authentication.

---

## 👨‍💻 Author

**Python Programming Project**

**Project Name:** Smart Grocery Store Management System

**Purpose:** Educational project demonstrating Python programming concepts and real-world application development.

---

⭐ Thank you for exploring the Smart Grocery Store Management System!