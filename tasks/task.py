class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name.upper().strip()   # string cleaning
        self.price = price
        self.quantity = quantity
        self.category = category

    def __str__(self):
        return f"{self.name} - Rs.{self.price} ({self.quantity} left)"