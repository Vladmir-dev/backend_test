from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from cachetools import TTLCache
from src.database import get_db
from src.dependencies.auth import get_current_user
from src.schemas.post import PostCreate, PostListResponse
from src.services.post import create_post, get_user_posts, get_post_by_id, delete_post

router = APIRouter()
cache = TTLCache(maxsize=100, ttl=300)  # 5-minute cache

@router.post("/posts", response_model=dict)
async def add_post(request: Request, post: PostCreate, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    """AddPost endpoint: Creates a new post for the authenticated user"""
    content_length = int(request.headers.get("content-length", 0))
    if content_length > 1048576:  # 1MB
        raise HTTPException(status_code=400, detail="Payload exceeds 1MB limit")
    
    db_post = create_post(db, post.text, user_id)
    return {"postID": db_post.id}

@router.get("/posts", response_model=PostListResponse)
def get_posts(user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    """GetPosts endpoint: Retrieves all posts for the authenticated user with caching"""
    cache_key = f"posts_{user_id}"
    if cache_key in cache:
        return {"posts": cache[cache_key]}
    
    posts = get_user_posts(db, user_id)
    cache[cache_key] = posts
    return {"posts": posts}

@router.delete("/posts/{post_id}")
def delete_post(post_id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    """DeletePost endpoint: Deletes a specific post for the authenticated user"""
    post = get_post_by_id(db, post_id, user_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found or not authorized")
    delete_post(db, post)
    return {"message": "Post deleted successfully"}
