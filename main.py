import json
from pathlib import Path
from product import Product
from inventory import Inventory

DATA_FILE = Path("inventory.json")


def load_inventory():
    inventory = Inventory()

    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            products = json.load(file)

        for item in products:
            product = Product(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"]
            )
            inventory.add_product(product)

    return inventory


def save_inventory(inventory):
    products = [
        product.to_dict()
        for product in inventory.get_products()
    ]

    with open(DATA_FILE, "w") as file:
        json.dump(products, file, indent=4)

    print("Inventory saved successfully.")


def main():
    inventory = load_inventory()

    while True:
        print("\n=== Inventory Management System ===")
        print("1. Display all products")
        print("2. Add a product")
        print("3. Update stock")
        print("4. Search for a product")
        print("5. Save inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            product_id = input("Enter product ID: ")

            if inventory.search_product(product_id):
                print("Product ID already exists.")
                continue

            name = input("Enter product name: ")

            try:
                price = float(input("Enter price: "))
                stock = int(input("Enter stock quantity: "))

                if price < 0 or stock < 0:
                    print("Price and stock cannot be negative.")
                    continue

                product = Product(
                    product_id, name, price, stock
                )
                inventory.add_product(product)
                print("Product added successfully.")

            except ValueError:
                print("Please enter a valid price and stock quantity.")

        elif choice == "3":
            product_id = input("Enter product ID: ")
            product = inventory.search_product(product_id)

            if product:
                try:
                    quantity = int(input("Enter new stock quantity: "))

                    if quantity < 0:
                        print("Stock cannot be negative.")
                    else:
                        product.update_stock(quantity)
                        print("Stock updated successfully.")

                except ValueError:
                    print("Please enter a valid whole number.")
            else:
                print("Product not found.")

        elif choice == "4":
            product_id = input("Enter product ID: ")
            product = inventory.search_product(product_id)

            if product:
                product.display_information()
            else:
                print("Product not found.")

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            save_inventory(inventory)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
