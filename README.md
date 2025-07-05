FastAPI Authentication App
A scalable FastAPI application with user authentication using JWT and SQLAlchemy.
Setup

Clone the repository:
git clone <repository-url>
cd project


Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Create a .env file:
DATABASE_URL=sqlite:///./users.db
SECRET_KEY=your-secret-key-here  # Generate with: openssl rand -hex 32
ACCESS_TOKEN_EXPIRE_MINUTES=30


Run the application:
uvicorn app.main:app --reload


Access the API:

Swagger UI: http://127.0.0.1:8000/docs
Register: POST /auth/register
Login: POST /auth/login
Get current user: GET /users/me



Testing
Run tests with pytest:
pytest tests/

Database

Uses SQLite by default (users.db).
To use PostgreSQL, update DATABASE_URL in .env (e.g., postgresql://user:password@localhost/dbname) and install psycopg2.

Security

Passwords are hashed using bcrypt.
JWT tokens are used for authentication.
Replace SECRET_KEY with a secure value in production.

# python-sql
