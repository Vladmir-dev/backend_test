from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas.user import UserCreate, UserLogin
from src.models.user import User
from src.services.auth import generate_token

router = APIRouter()

@router.post("/signup", response_model=dict)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    """Signup endpoint: Creates a new user and returns a JWT token"""
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(email=user.email, password=user.password)  # In production, hash password
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    token = generate_token(new_user.id)
    return {"token": token}

@router.post("/login", response_model=dict)
def login(user: UserLogin, db: Session = Depends(get_db)):
    """Login endpoint: Authenticates user and returns a JWT token"""
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or db_user.password != user.password:  # In production, compare hashed passwords
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = generate_token(db_user.id)
    return {"token": token}
