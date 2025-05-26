# Database configuration
DATABASE_URL = "mysql+mysqlconnector://root:testuser@localhost:3306/task_db"
# JWT configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

# Cache configuration (5 minutes TTL)
CACHE_TTL = 300
