
````markdown
# Lucid Task Submission

A FastAPI web application following the MVC pattern, interfacing with MySQL via SQLAlchemy. It features token-based authentication, caching, and request validation.

---

## 🚀 Project Structure

```text
src/
├── main.py           # FastAPI app entry point
├── config.py         # Configuration settings
├── database.py       # Database setup
├── models/           # SQLAlchemy models for User and Post
├── schemas/          # Pydantic schemas for validation
├── services/         # Business logic for authentication and post operations
├── routes/           # API endpoints
└── dependencies/     # Dependency injection for authentication
````

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/tumwebazepius/lucid-task-submission.git
cd lucid-task-submission
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL

* Install MySQL and create a database named `task_db`.
* Update `src/config.py` with your MySQL credentials:

```python
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://your_username:your_password@localhost:3306/task_db"
```

### 4. Run the Application

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

The app will be available at: [http://localhost:8000](http://localhost:8000)

---

## 🔗 Endpoints

| Method | Endpoint           | Description                         | Auth Required |
| ------ | ------------------ | ----------------------------------- | ------------- |
| POST   | `/signup`          | Create a new user and get a token   | ❌             |
| POST   | `/login`           | Login and retrieve a token          | ❌             |
| POST   | `/posts`           | Create a post                       | ✅             |
| GET    | `/posts`           | Retrieve user posts (cached 5 mins) | ✅             |
| DELETE | `/posts/{post_id}` | Delete a specific post              | ✅             |

---

## 🧪 Testing

You can use **Postman** or `curl`:

### Signup

```bash
curl -X POST http://localhost:8000/signup \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "Pass123word"}'
```

### Login

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "Pass123word"}'
```

### Add Post

```bash
curl -X POST http://localhost:8000/posts \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"text": "My first post"}'
```

### Get Posts

```bash
curl -X GET http://localhost:8000/posts \
  -H "Authorization: Bearer <token>"
```

### Delete Post

```bash
curl -X DELETE http://localhost:8000/posts/1 \
  -H "Authorization: Bearer <token>"
```

---

## ⚠️ Notes

* **Passwords are stored in plaintext** for simplicity. For production, use secure hashing (e.g., `bcrypt`).
* If MySQL setup fails, you can switch to **SQLite** by updating `DATABASE_URL` in `config.py`:

```python
SQLALCHEMY_DATABASE_URL = "sqlite:///task.db"
```

---

Happy coding! 🎯

```

Let me know if you'd like this turned into a `README.md` file or if you want badges (like Python version, license, etc.) added to the top.
```

