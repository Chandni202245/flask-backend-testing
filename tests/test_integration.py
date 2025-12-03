import requests

BASE = "http://127.0.0.1:5000"

def test_user_and_product_flow():
    # register user
    requests.post(BASE + "/register", json={"username": "flow", "password": "pass"})
    # login
    login = requests.post(BASE + "/login", json={"username": "flow", "password": "pass"})
    assert login.status_code == 200

    # add product
    prod = requests.post(BASE + "/products", json={"name": "Mouse", "price": 299})
    assert prod.status_code == 201

    # delete product
    pid = prod.json().get("id")
    delete = requests.delete(BASE + f"/products/{pid}")
    assert delete.status_code == 200
