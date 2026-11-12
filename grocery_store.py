
# ==========================================
# SMART GROCERY STORE MANAGEMENT SYSTEM
# ==========================================

# Step 1: Store Products in a List of Dictionaries

products = [
    {
        "id": 101,
        "name": "Milk",
        "category": "Dairy",
        "price": 250,
        "stock": 20
    },
    {
        "id": 102,
        "name": "Bread",
        "category": "Bakery",
        "price": 150,
        "stock": 15
    },
    {
        "id": 103,
        "name": "Rice",
        "category": "Food",
        "price": 300,
        "stock": 10
    }
]

# Separate list for sales records
sales_records = []


# Step 2: Function to find product by ID

def find_product_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product

    return None


# Step 3: Function to add a new product

def add_product():
    print("\n--- Add New Product ---")

    try:
        product_id = int(input("Enter Product ID: "))

        # Check duplicate product ID
        if find_product_by_id(product_id) is not None:
            print("Error: Product ID already exists!")
            return

        name = input("Enter Product Name: ").strip()
        category = input("Enter Category: ").strip()
        price = float(input("Enter Price: "))
        stock = int(input("Enter Available Stock: "))

        # Validate product information
        if product_id <= 0 or name == "" or category == "":
            print("Invalid product information!")
            return

        if price <= 0 or stock < 0:
            print("Price must be positive and stock cannot be negative!")
            return

        # Create product dictionary
        new_product = {
            "id": product_id,
            "name": name,
            "category": category,
            "price": price,
            "stock": stock
        }

        # Add dictionary to products list
        products.append(new_product)

        print("Product added successfully!")

    except ValueError:
        print("Invalid input! Please enter correct values.")


# Step 4: Function to display all products

def view_products():
    print("\n--- All Available Products ---")

    if len(products) == 0:
        print("No products available.")
        return

    for product in products:
        print("------------------------------")
        print("Product ID:", product["id"])
        print("Name:", product["name"])
        print("Category:", product["category"])
        print("Price: Rs.", product["price"])
        print("Available Stock:", product["stock"])


# Step 5: Function to search a product

def search_product():
    print("\n--- Search Product ---")

    search_value = input("Enter Product Name or ID: ").strip()

    found = False

    for product in products:

        if (search_value.lower() == product["name"].lower()
                or search_value == str(product["id"])):

            print("\nProduct Found!")
            print("Product ID:", product["id"])
            print("Name:", product["name"])
            print("Category:", product["category"])
            print("Price: Rs.", product["price"])
            print("Available Stock:", product["stock"])

            found = True
            break

    if found == False:
        print("Product not found!")


# Step 6: Function to update product stock

def update_stock():
    print("\n--- Update Product Stock ---")

    try:
        product_id = int(input("Enter Product ID: "))

        product = find_product_by_id(product_id)

        if product is None:
            print("Product not found!")
            return

        print("Current Stock:", product["stock"])
        print("1. Add More Stock")
        print("2. Set New Stock Quantity")

        choice = input("Enter your choice: ")

        if choice == "1":
            quantity = int(input("Enter quantity to add: "))

            if quantity <= 0:
                print("Quantity must be positive!")
                return

            product["stock"] += quantity

        elif choice == "2":
            quantity = int(input("Enter new stock quantity: "))

            if quantity < 0:
                print("Stock cannot be negative!")
                return

            product["stock"] = quantity

        else:
            print("Invalid choice!")
            return

        print("Stock updated successfully!")
        print("Updated Stock:", product["stock"])

    except ValueError:
        print("Invalid input! Enter numbers only.")


# Step 7: Function to process customer sale

def process_sale():
    print("\n--- Process Customer Sale ---")

    try:
        product_id = int(input("Enter Product ID: "))

        product = find_product_by_id(product_id)

        if product is None:
            print("Product not found!")
            return

        quantity = int(input("Enter Purchase Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        # Check available stock
        if quantity > product["stock"]:
            print("Insufficient Stock!")
            print("Available Stock:", product["stock"])
            return

        # Calculate total amount
        total_amount = product["price"] * quantity

        # Deduct sold quantity from stock
        product["stock"] -= quantity

        # Create sales record dictionary
        sale = {
            "id": product["id"],
            "name": product["name"],
            "quantity": quantity,
            "total": total_amount
        }

        # Save sale in sales records list
        sales_records.append(sale)

        # Display purchase summary
        print("\n--- Purchase Summary ---")
        print("Product Name:", product["name"])
        print("Product ID:", product["id"])
        print("Quantity Sold:", quantity)
        print("Price per Item: Rs.", product["price"])
        print("Total Amount: Rs.", total_amount)
        print("Remaining Stock:", product["stock"])
        print("Sale Completed Successfully!")

    except ValueError:
        print("Invalid input! Enter numbers only.")


# Step 8: Function to display sales records

def view_sales():
    print("\n--- Sales Records ---")

    if len(sales_records) == 0:
        print("No sales records available.")
        return

    for sale in sales_records:
        print("------------------------------")
        print("Product ID:", sale["id"])
        print("Product Name:", sale["name"])
        print("Quantity Sold:", sale["quantity"])
        print("Total Amount: Rs.", sale["total"])


# Step 9: Function to generate store report

def generate_report():
    print("\n--- STORE REPORT ---")

    if len(products) == 0:
        print("No products available for report.")
        print("Total Sales Transactions:", len(sales_records))

        revenue = 0
        for sale in sales_records:
            revenue += sale["total"]

        print("Total Revenue: Rs.", revenue)
        return

    total_stock = 0
    total_revenue = 0

    # Calculate total available stock
    for product in products:
        total_stock += product["stock"]

    # Calculate total revenue
    for sale in sales_records:
        total_revenue += sale["total"]

    print("Total Number of Products:", len(products))
    print("Total Available Stock:", total_stock)
    print("Total Sales Transactions:", len(sales_records))
    print("Total Revenue: Rs.", total_revenue)

    # Display products with stock below 5
    print("\nProducts with Stock Below 5:")

    low_stock_found = False

    for product in products:
        if product["stock"] < 5:
            print(product["name"], "- Stock:", product["stock"])
            low_stock_found = True

    if low_stock_found == False:
        print("No low stock products.")

    # Find highest and lowest price products
    highest_product = products[0]
    lowest_product = products[0]

    for product in products:

        if product["price"] > highest_product["price"]:
            highest_product = product

        if product["price"] < lowest_product["price"]:
            lowest_product = product

    print("\nHighest Price Product:")
    print(highest_product["name"], "- Rs.", highest_product["price"])

    print("\nLowest Price Product:")
    print(lowest_product["name"], "- Rs.", lowest_product["price"])


# Step 10: Main Menu

def display_menu():
    print("\n====================================")
    print("     SMART GROCERY STORE SYSTEM")
    print("====================================")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit")


# Step 11: Run the application

while True:

    display_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        update_stock()

    elif choice == "5":
        process_sale()

    elif choice == "6":
        view_sales()

    elif choice == "7":
        generate_report()

    elif choice == "8":
        print("Thank you for using Smart Grocery Store!")
        break

    else:
        print("Invalid choice! Please select 1 to 8.")
