from tasks.task import Product

class InventoryManager:
    def __init__(self):
        self.products = []
        self.cart = []

    def load_products(self):
        try:
            with open("inventory.txt", "r") as f:
                for line in f:
                    name, price, qty, category = line.strip().split(",")
                    self.products.append(
                        Product(name, float(price), int(qty), category)
                    )
        except FileNotFoundError:
            print("Inventory file not found!")

    def show_products(self):
        for p in self.products:
            print(p)

    def add_to_cart(self, name):
        for p in self.products:
            print(p.name, name)
            if p.name == name:
                if p.quantity > 0:
                    self.cart.append(
                        Product(p.name, p.price, 1, p.category)
                    )
                    p.quantity -= 1
                    print("Added to cart!")
                    return
                else:
                    print("Out of stock!")
                    return
        print("Product not found!")

    def show_categories(self):
        categories = {p.category for p in self.products}  # set
        print("Categories:", categories)

    def view_cart(self):
        if not self.cart:
            print("Cart is empty!")
            return

        print("\n--- Your Cart ---")
        total = 0

        for item in self.cart:
            print(f"{item.name} - Rs.{item.price}")
            total += item.price

        print(f"Total so far: Rs.{total}")