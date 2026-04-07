# 🚀 Clean Python FastAPI - Product API

A scalable backend REST API built with **FastAPI** following **Clean Architecture principles**.

This project demonstrates how to structure a production-ready backend separating business logic, infrastructure, and presentation layers.

---

## 🏗️ Architecture Overview

This project is based on **Clean Architecture**:

- **Domain Layer**
  - Core business rules
  - Entities and Value Objects
  - No external dependencies

- **Application Layer**
  - Use cases (business logic orchestration)
  - DTOs and interfaces
  - Service coordination

- **Infrastructure Layer**
  - Persistence implementation
  - Storage handling
  - Repository implementations

- **Presentation Layer**
  - FastAPI controllers
  - Request/Response handling
  - API routing

---

## 📦 Features

- Create product
- Get all products
- Get product by ID
- Delete product
- Domain validation using Value Objects
- Repository pattern
- Dependency injection (manual)
- Clean separation of concerns

---

## 🧠 Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

---

## 📁 Project Structure

domain/
application/
infrastructure/
presentation/
main.py

---

## 🚀 How to Run

### 1. Clone repository
git clone https://github.com/your-username/clean-python-fastapi.git
cd clean-python-fastapi

### 2. Create virtual environment
python -m venv venv

### 3. Activate environment (Windows)
venv\Scripts\activate

### 4. Install dependencies
pip install -r requirements.txt

### 5. Run the API
uvicorn main:app --reload

---

## 📌 API Endpoints

### Create Product
POST /products

### Get All Products
GET /products

### Get Product by ID
GET /products/{product_id}

### Delete Product
DELETE /products/{product_id}

---

## 📤 Example Request

{
  "id": 1,
  "name": "Laptop",
  "price": 1500,
  "stock": 10
}

---

## 📥 Example Response

{
  "data": {
    "id": 1,
    "name": "Laptop",
    "price": 1500,
    "stock": 10
  },
  "message": "Product created successfully"
}

---

## 🎯 Purpose of this project

This project was built to demonstrate:

- Scalable backend design
- Clean Architecture principles
- Separation of concerns
- Maintainable code structure
- Real-world backend patterns

---

## 👨‍💻 Author

Nimer Cerna Espinoza  
Backend Developer (Python / .NET / PHP)

---

## ⭐ Notes

This project is for learning and portfolio demonstration purposes.
