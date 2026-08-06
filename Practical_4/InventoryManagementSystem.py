# Inventory Management System
 
inventory = {}
 
def add_product(name, quantity):
    inventory[name] = quantity
    print(name, "added successfully.")
 
def update_product(name, quantity):
    if name in inventory:
        inventory[name] = quantity
        print(name, "quantity updated.")
 
        if inventory[name] == 0:
            del inventory[name]
            print(name, "removed from inventory (Sold Out).")
    else:
        print("Product not found.")
 
def highest_stock():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        product = max(inventory, key=inventory.get)
        print("Product with highest stock:", product)
        print("Quantity:", inventory[product])
 
def display_inventory():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for product, quantity in inventory.items():
            print(product, ":", quantity)
 
def total_products():
    print("Total Unique Products:", len(inventory))
 
while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Product")
    print("2. Update Product Quantity")
    print("3. Display Inventory")
    print("4. Display Product with Highest Stock")
    print("5. Display Total Unique Products")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        add_product(name, quantity)

    elif choice == "2":
        name = input("Enter product name: ")
        quantity = int(input("Enter new quantity: "))
        update_product(name, quantity)

    elif choice == "3":
        display_inventory()

    elif choice == "4":
        highest_stock()

    elif choice == "5":
        total_products()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")