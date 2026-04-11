
# File handling
def save_receipt(cart):
    try:
        with open("receipt.txt", "w") as f:
            total = 0
            for item in cart:
                f.write(f"{item.name} - Rs.{item.price}\n")
                total += item.price
            f.write(f"\nTotal: Rs.{total}")
    except Exception as e:
        print("Error saving receipt:", e)

def update_inventory(cart):
    try:
        with open("inventory.txt", "r") as f:
            lines = f.readlines()

        new_lines = []

        for line in lines:
            name, price, qty, category = line.strip().split(",")

            for item in cart:
                if item.name == name:
                    qty = str(int(qty) - 1)

            new_lines.append(f"{name},{price},{qty},{category}\n")

        with open("inventory.txt", "w") as f:
            f.writelines(new_lines)

    except Exception as e:
        print("Error updating inventory:", e)