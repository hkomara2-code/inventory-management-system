from tasks.task_manager import InventoryManager
from utils.helpers import save_receipt

def main():
    manager = InventoryManager()
    manager.load_products()

    while True:
        print("\n1. Show Products")
        print("2. Add to Cart")
        print("3. Show Categories")
        print("4. View cart")
        print("5. Generate Recipt")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.show_products()

        elif choice == "2":
            item = input("Enter product name: ")
            manager.add_to_cart(item)

        elif choice == "3":
            manager.show_categories()

        elif choice == "4":
            manager.view_cart()

        elif choice == "5":
            save_receipt(manager.cart)
            print("Receipt generated!")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
