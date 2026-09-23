from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "watch_store_secret_key"


# -----------------------------
# WATCH PRODUCTS
# -----------------------------

watches = [
    {
        "id": 1,
        "name": "Classic Black",
        "price": 2999,
        "category": "Classic",
        "image": "watch1.jpg",
        "description": "A stylish black watch designed for everyday elegance."
    },
    {
        "id": 2,
        "name": "Golden Royale",
        "price": 4499,
        "category": "Luxury",
        "image": "watch2.jpg",
        "description": "A premium golden watch with a sophisticated luxury design."
    },
    {
        "id": 3,
        "name": "Ocean Blue",
        "price": 3499,
        "category": "Sport",
        "image": "watch3.jpg",
        "description": "A sporty blue watch perfect for active lifestyles."
    },
    {
        "id": 4,
        "name": "Silver Edge",
        "price": 3999,
        "category": "Classic",
        "image": "watch4.jpg",
        "description": "Minimal silver design with a modern and clean appearance."
    },
    {
        "id": 5,
        "name": "Midnight Chrono",
        "price": 5499,
        "category": "Chronograph",
        "image": "watch5.jpg",
        "description": "A bold chronograph watch for those who love premium styling."
    },
    {
        "id": 6,
        "name": "Urban Green",
        "price": 3299,
        "category": "Sport",
        "image": "watch6.jpg",
        "description": "A modern green watch made for everyday urban adventures."
    }
]


# -----------------------------
# HOME PAGE
# -----------------------------

@app.route("/")
def home():
    featured_watches = watches[:4]

    return render_template(
        "index.html",
        watches=featured_watches
    )


# -----------------------------
# PRODUCTS PAGE
# -----------------------------

@app.route("/products")
def products():

    search = request.args.get("search", "").lower()
    category = request.args.get("category", "")

    filtered_watches = watches

    if search:
        filtered_watches = [
            watch for watch in filtered_watches
            if search in watch["name"].lower()
        ]

    if category:
        filtered_watches = [
            watch for watch in filtered_watches
            if watch["category"] == category
        ]

    return render_template(
        "products.html",
        watches=filtered_watches
    )


# -----------------------------
# PRODUCT DETAILS
# -----------------------------

@app.route("/product/<int:product_id>")
def product(product_id):

    selected_watch = next(
        (watch for watch in watches if watch["id"] == product_id),
        None
    )

    if selected_watch is None:
        return "Product not found", 404

    return render_template(
        "product.html",
        watch=selected_watch
    )


# -----------------------------
# ADD TO CART
# -----------------------------

@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):

    cart = session.get("cart", [])

    if product_id not in cart:
        cart.append(product_id)

    session["cart"] = cart

    flash("Watch added to your cart!")

    return redirect(url_for("products"))


# -----------------------------
# CART
# -----------------------------

@app.route("/cart")
def cart():

    cart_ids = session.get("cart", [])

    cart_items = [
        watch for watch in watches
        if watch["id"] in cart_ids
    ]

    total = sum(
        watch["price"]
        for watch in cart_items
    )

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )


# -----------------------------
# REMOVE FROM CART
# -----------------------------

@app.route("/remove-from-cart/<int:product_id>")
def remove_from_cart(product_id):

    cart = session.get("cart", [])

    if product_id in cart:
        cart.remove(product_id)

    session["cart"] = cart

    return redirect(url_for("cart"))


# -----------------------------
# CONTACT
# -----------------------------

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print("New Contact Message")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        flash("Thank you! Your message has been received.")

        return redirect(url_for("contact"))

    return render_template("contact.html")


# -----------------------------
# RUN SERVER
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)