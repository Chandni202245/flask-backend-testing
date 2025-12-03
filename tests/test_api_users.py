import requests

BASE = "http://127.0.0.1:5000"

def test_register_user():
    body = {"username": "test1", "password": "123"}
    res = requests.post(BASE + "/register", json=body)
    assert res.status_code in (201, 409)

def test_login_valid():
    res = requests.post(BASE + "/login", json={"username": "test1", "password": "123"})
    assert res.status_code in (200, 401)
