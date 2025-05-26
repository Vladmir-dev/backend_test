from typing import List, Optional
from sqlalchemy.orm import Session
from src.models import Post

def create_post(db: Session, text: str, user_id: int) -> Post:
    """Create a new post in the database"""
    db_post = Post(text=text, user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_user_posts(db: Session, user_id: int) -> List[Post]:
    """Retrieve all posts for a user from the database"""
    return db.query(Post).filter(Post.user_id == user_id).all()

def get_post_by_id(db: Session, post_id: int, user_id: int) -> Optional[Post]:
    """Retrieve a specific post by ID for a user"""
    return db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()

def delete_post(db: Session, post: Post):
    """Delete a post from the database"""
    db.delete(post)
    db.commit()
