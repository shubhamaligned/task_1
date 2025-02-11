# E-commerce API

## Description
This is a FastAPI-based e-commerce API that allows users to manage products and orders. It includes full CRUD operations and database persistence using PostgreSQL.

## Features
- Create, read, update, and delete products.
- Create, read, update, and delete orders.
- Update order status (e.g., pending → shipped).
- Uses PostgreSQL as the database.
- Includes API documentation with Swagger UI.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/shubhamaligned/task_1.git
cd task_1
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3 Run the FastAPI Server**
```sh
uvicorn main:app --reload
```
The API will be available at:  
🔹 **http://127.0.0.1:8000**

##  API Documentation
FastAPI automatically generates interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---