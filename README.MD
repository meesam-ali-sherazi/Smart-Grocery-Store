# Smart Grocery Store Management System

**Python Programming Project | Lists & Dictionaries**

---

## Student Information

- **Student Name:** Meesam Ali Sherazi
- **Project Name:** Smart Grocery Store Management System
- **Programming Language:** Python 3
- **Project Type:** Console-Based Application

## 1. Project Overview

The Smart Grocery Store Management System is a Python-based console application designed to manage grocery store operations efficiently.

The system allows users to manage products, monitor available stock, process customer sales, search for products, and generate sales reports. It uses Python lists and dictionaries to store and organize product information and sales records.

The main objective of this project is to demonstrate the practical use of Python data structures, functions, loops, and conditional statements in a real-world business scenario.

## 2. Project Features

### Product Management
- Add new products to the inventory.
- Display all available products.
- Search for products using their unique Product ID.
- Update product stock quantities.
- Prevent duplicate Product IDs.

### Sales Management
- Process customer purchases.
- Calculate the total bill automatically.
- Update inventory after each sale.
- Maintain a record of sales transactions.
- Prevent sales when the requested quantity exceeds available stock.

### Inventory and Sales Reports
- Display total number of products.
- Calculate total available stock.
- Display total sales transactions.
- Calculate total sales revenue.
- Identify low-stock products.
- Find the highest-priced and lowest-priced products.

## 3. Python Concepts and Techniques Used

The following Python concepts are implemented in this project:

- **Lists:** Used to store multiple products and sales records.
- **Dictionaries:** Used to organize product details such as ID, name, category, price, and stock.
- **Functions:** Used to divide the program into reusable and manageable sections.
- **Parameters and Return Values:** Used to pass information between functions and return results.
- **Loops:** Used to display menus and repeatedly execute program operations.
- **Conditional Statements:** Used to make decisions based on user input and product conditions.
- **Input Validation:** Used to ensure that users enter valid information.
- **Exception Handling:** Used to handle invalid inputs and prevent unexpected program termination.
- **Dictionary Operations:** Used to access and update product information.
- **String Formatting:** Used to display information in a clear and readable format.

## 4. How to Run the Program

Follow these steps to run the application:

1. Install Python 3 on your computer.
2. Download or clone this project repository.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.
5. Execute the following command:

```bash
py grocery_store.py
```

The main menu will appear, allowing users to select and perform different grocery store operations.

## 5. Sample Input and Output

### Initial Product Inventory

| Product ID | Product Name | Category | Price (Rs.) | Stock |
|---|---|---|---:|---:|
| 101 | Milk | Dairy | 250 | 20 |
| 102 | Bread | Bakery | 150 | 15 |
| 103 | Rice | Food | 300 | 10 |

### Sample Sales Transaction

**Input:**
- Product ID: 101
- Quantity: 2

**Output:**
- Product Name: Milk
- Total Bill: Rs. 500
- Remaining Stock: 18

### Sample Store Report

- Total Products: 3
- Total Available Stock: 43
- Total Sales Transactions: 1
- Total Sales Revenue: Rs. 500
- Highest-Priced Product: Rice (Rs. 300)
- Lowest-Priced Product: Bread (Rs. 150)

## 6. Project Structure

```text
Smart-Grocery-Store/
│
├── grocery_store.py
│
└── README.md
```

## 7. Conclusion

The Smart Grocery Store Management System demonstrates how Python can be used to develop a simple and practical inventory and sales management application.

This project provides hands-on experience with lists, dictionaries, functions, loops, conditional statements, and exception handling. It also improves problem-solving and programming skills by applying these concepts to a real-world grocery store management scenario.

---

**End of Project Documentation**