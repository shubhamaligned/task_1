# FastAPI Blogging API

This is a FastAPI-based RESTful API for creating posts and comments. The API allows users to create posts, add comments to posts, and retrieve posts along with their associated comments.

## 🚀 Features
- Create blog posts
- Retrieve all posts with pagination and sorting
- Add comments to posts
- Retrieve a post along with its comments

## 🛠️ Tech Stack
- **FastAPI** (Backend API)
- **MongoDB** (Database)
- **Pydantic** (Data validation & serialization)
- **Pytest** (Testing framework)

---

## 🏗️ Setup and Installation

### 1️⃣ Clone the Repository
```bash
git clone git clone https://github.com/shubhamaligned/task_1.git
cd task_1/task_2
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the FastAPI Server
```bash
uvicorn app.main:app --reload
```
- The API will be available at `http://127.0.0.1:8000`
- Interactive Swagger UI: `http://127.0.0.1:8000/docs`

---

## 🔥 API Endpoints

### 📌 Posts
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/posts/` | Create a new post |
| `GET` | `/posts/?skip=0&limit=10&sort_by=created_at&order=-1` | Get paginated posts |
| `GET` | `/posts/{post_id}` | Get a post by ID |

### 📌 Comments
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/comments/` | Add a comment to a post |
| `GET` | `/comments/{post_id}` | Retrieve comments for a post |

---

## ✅ Running Tests
We use **pytest** for testing. Run the tests using:
```bash
pytest tests/
```

---

## 📄 License
MIT License © 2025