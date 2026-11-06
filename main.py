import json
import os  

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

FILE_NAME = "inventory.json"

def save_inventory(inventory):
    data = [product.to_dict() for product in inventory.get_products()]

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")


def load_inventory():
    inventory = Inventory()

    if not os.path.exists(FILE_NAME):
        return inventory

    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    for item in data:
        if item["type"] == "physical":
            product = PhysicalProduct(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"],
                item["weight"]
            )

        elif item["type"] == "digital":
            product = DigitalProduct(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"],
                item["download_size"]
            )

        else:
            continue

        inventory.add_product(product)

    return inventory


def add_product(inventory):
    print("\n1. Physical Product")
    print("2. Digital Product")

    choice = input("Choose product type: ")

    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))

    if choice == "1":
        weight = float(input("Enter product weight (kg): "))
        product = PhysicalProduct(
            product_id, name, price, stock, weight
        )

    elif choice == "2":
        download_size = float(input("Enter download size (MB): "))
        product = DigitalProduct(
            product_id, name, price, stock, download_size
        )

    else:
        print("Invalid product type.")
        return

    inventory.add_product(product)
    print("Product added successfully.")


def update_product(inventory):
    product_id = input("Enter product ID: ")
    product = inventory.search_product(product_id)

    if product:
        quantity = int(input("Enter new stock quantity: "))
        product.update_stock(quantity)
        print("Stock updated successfully.")
    else:
        print("Product not found.")


def search_product(inventory):
    product_id = input("Enter product ID: ")
    product = inventory.search_product(product_id)

    if product:
        product.display_information()
        print(product.get_fulfilment_info())

        if isinstance(product, PhysicalProduct):
            print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
    else:
        print("Product not found.")


def display_products(inventory):
    inventory.display_all()


def main():
    inventory = load_inventory()

    while True:
        print("\nInventory Management System")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Product Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_products(inventory)

        elif choice == "2":
            add_product(inventory)

        elif choice == "3":
            update_product(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            save_inventory(inventory)
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
    