# Flask Backend Testing Project | Python + Pytest + API + Integration Testing

This project demonstrates complete **Backend Testing** using Flask APIs, Pytest, and Requests.  
It includes **API Testing, Unit Testing, Integration Testing, Manual Test Cases, and Negative Testing** — aligned with QA Engineer Intern roles such as **GeeksforGeeks**, product-based startups, and backend QA teams.

---

## 🚀 Features

- 🟦 **Flask Backend**
- 🟧 **API Testing** using Pytest + Requests
- 🟩 **Unit Tests** for backend functions
- 🟨 **Integration Tests** (user + product flow)
- 🟥 **Negative Testing** with invalid inputs
- 📝 **Manual Test Cases** included
- 📄 File-based mock database (`database.json`)

---

## 📁 Project Structure

flask-backend-testing/
│── app.py
│── requirements.txt
│── database.json
│── .gitignore
│── manual_test_cases.md
│── tests/
│ ├── test_unit.py
│ ├── test_api_users.py
│ ├── test_api_products.py
│ ├── test_integration.py


---

## Tech Stack

- **Python 3**
- **Flask**
- **Pytest**
- **Requests library**
- **JSON data storage**

###  Start Flask Server


python app.py

Server runs on:  
👉 **http://127.0.0.1:5000**

---

##  Running Tests

To run all tests:

This executes:

- ✔ Unit tests  
- ✔ API tests  
- ✔ Integration tests  
- ✔ Negative tests  

---

##  API Endpoints

###  Register User
POST /register

###  Login User

POST /login

###  Get All Products

GET /products

###  Add Product

POST /products

###  Delete Product

DELETE /products/<id>







