from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.database import Base

class Post(Base):
    """SQLAlchemy model for posts table"""
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(1048576), nullable=False)  # 1MB limit in DB
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="posts")
