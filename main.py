from flask import Flask, render_template, redirect, request
from tasks.task_manager import InventoryManager
from utils.helpers import save_receipt, update_inventory
app = Flask(__name__)

manager = InventoryManager()
manager.load_products()


# 🔷 HOME → SHOW CATEGORIES
@app.route("/")
def home():
    categories = list({p.category for p in manager.products})
    return render_template("index.html", categories=categories)


# 🔷 SHOW PRODUCTS OF SELECTED CATEGORY
@app.route("/products/<category>")
def products(category):
    items = [p for p in manager.products if p.category == category]
    return render_template("products.html", items=items, category=category)


# 🔷 ADD TO CART
@app.route("/add/<name>")
def add(name):
    manager.add_to_cart(name)
    return redirect(request.referrer)


# 🔷 VIEW CART
@app.route("/cart")
def cart():
    total = sum(item.price for item in manager.cart)
    return render_template("cart.html", cart=manager.cart, total=total)


# 🔷 CHECKOUT
@app.route("/checkout")
def checkout():
    save_receipt(manager.cart)
    manager.cart.clear()
    return redirect("/receipt")


# 🔷 VIEW RECEIPT
@app.route("/receipt")
def receipt():
    try:
        with open("receipt.txt", "r", encoding="utf-8") as f:
            data = f.read()
    except:
        data = "No receipt found"
    return render_template("receipt.html", data=data)

@app.route("/payment")
def payment():
    update_inventory(manager.cart)   # 🔥 reduce stock
    manager.cart.clear()             # clear cart
    return render_template("payment.html")

if __name__ == "__main__":
    app.run(debug=True)