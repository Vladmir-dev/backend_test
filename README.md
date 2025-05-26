
Lucid Task Submission
A FastAPI web application following the MVC pattern, interfacing with MySQL via SQLAlchemy, with token-based authentication, caching, and validation.
Project Structure

src/main.py: FastAPI app entry point.
src/config.py: Configuration settings.
src/database.py: Database setup.
src/models/: SQLAlchemy models for User and Post.
src/schemas/: Pydantic schemas for validation.
src/services/: Business logic for authentication and post operations.
src/routes/: API endpoints.
src/dependencies/: Dependency injection for authentication.

Setup

Clone the Repository:git clone https://github.com/tumwebazepius/lucid-task-submission.git
cd lucid-task-submission


Install Dependencies:pip install -r requirements.txt


Configure MySQL:
Install MySQL and create a database named task_db.
Update src/config.py with your MySQL credentials (e.g., mysql+mysqlconnector://your_username:your_password@localhost:3306/task_db).


Run the Application:uvicorn src.main:app --host 0.0.0.0 --port 8000

The app will run at http://localhost:8000.

Endpoints

POST /signup: Create a user and get a token.
POST /login: Login and get a token.
POST /posts: Add a post (requires token).
GET /posts: Get user posts (requires token, cached for 5 minutes).
DELETE /posts/{post_id}: Delete a post (requires token).

Testing
Use Postman or curl:

Signup: curl -X POST http://localhost:8000/signup -H "Content-Type: application/json" -d '{"email": "test@example.com", "password": "Pass123word"}'
Login: curl -X POST http://localhost:8000/login -H "Content-Type: application/json" -d '{"email": "test@example.com", "password": "Pass123word"}'
AddPost: curl -X POST http://localhost:8000/posts -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"text": "My first post"}'
GetPosts: curl -X GET http://localhost:8000/posts -H "Authorization: Bearer <token>"
DeletePost: curl -X DELETE http://localhost:8000/posts/1 -H "Authorization: Bearer <token>"

Notes

Passwords are stored in plaintext for simplicity. In production, use hashing (e.g., bcrypt).
If MySQL setup fails, switch to SQLite by updating DATABASE_URL in config.py to sqlite:///task.db.

