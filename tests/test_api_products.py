import requests
BASE = "http://127.0.0.1:5000"

def test_add_product():
    body = {"name": "Keyboard", "price": 599}
    res = requests.post(BASE + "/products", json=body)
    assert res.status_code in (201, 400)

def test_get_products():
    res = requests.get(BASE + "/products")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
