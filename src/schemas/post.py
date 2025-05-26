from pydantic import BaseModel, constr, field_validator
from datetime import datetime
from typing import List

class PostCreate(BaseModel):
    """Pydantic schema for creating a post"""
    text: constr(max_length=1048576)  # 1MB limit

    @field_validator("text")
    def validate_size(cls, v):
        if len(v.encode('utf-8')) > 1048576:  # 1MB in bytes
            raise ValueError("Payload exceeds 1MB limit")
        return v

class PostResponse(BaseModel):
    """Pydantic schema for post response"""
    id: int
    text: str
    created_at: datetime

    class Config:
        orm_mode = True

class PostListResponse(BaseModel):
    """Pydantic schema for list of posts"""
    posts: List[PostResponse]
