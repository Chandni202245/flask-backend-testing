from app import read_db, write_db

def test_read_write_db():
    data = {"users": [{"username": "admin"}], "products": []}
    write_db(data)
    db = read_db()
    assert db["users"][0]["username"] == "admin"
