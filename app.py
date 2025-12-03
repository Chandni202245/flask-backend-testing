from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)

DB_FILE = "database.json"

# Initialize DB file
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({"users": [], "products": []}, f)

def read_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ----------- USER ENDPOINTS -------------

@app.route("/register", methods=["POST"])
def register():
    data = read_db()
    body = request.json

    if not body.get("username") or not body.get("password"):
        return jsonify({"error": "Invalid input"}), 400

    if body["username"] in [u["username"] for u in data["users"]]:
        return jsonify({"error": "User already exists"}), 409

    data["users"].append(body)
    write_db(data)
    return jsonify({"message": "User registered"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = read_db()
    body = request.json

    for user in data["users"]:
        if user["username"] == body.get("username") and user["password"] == body.get("password"):
            return jsonify({"message": "Login successful"}), 200

    return jsonify({"error": "Invalid credentials"}), 401


# ----------- PRODUCT ENDPOINTS -------------

@app.route("/products", methods=["GET"])
def get_products():
    data = read_db()
    return jsonify(data["products"]), 200


@app.route("/products", methods=["POST"])
def add_product():
    data = read_db()
    body = request.json

    if not body.get("name") or not body.get("price"):
        return jsonify({"error": "Invalid product data"}), 400

    product = {
        "id": len(data["products"]) + 1,
        "name": body["name"],
        "price": body["price"]
    }

    data["products"].append(product)
    write_db(data)
    return jsonify(product), 201


@app.route("/products/<int:pid>", methods=["DELETE"])
def delete_product(pid):
    data = read_db()
    products = data["products"]

    for product in products:
        if product["id"] == pid:
            products.remove(product)
            write_db(data)
            return jsonify({"message": "Product deleted"}), 200

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
