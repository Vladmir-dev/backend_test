from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database import Base

class User(Base):
    """SQLAlchemy model for users table"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    posts = relationship("Post", back_populates="user")
