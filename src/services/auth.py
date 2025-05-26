from datetime import datetime, timedelta
import jwt
from src.config import SECRET_KEY, ALGORITHM, TOKEN_EXPIRE_MINUTES

def generate_token(user_id: int) -> str:
    """Generate a JWT token for the user"""
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> int:
    """Verify JWT token and return user ID"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise ValueError("Invalid token")
        return user_id
    except jwt.PyJWTError as e:
        raise ValueError(f"Invalid or expired token: {str(e)}")
