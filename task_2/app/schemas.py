from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PostSchema(BaseModel):
    title: str
    content: str
    author: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class PostUpdateSchema(BaseModel):
    title: Optional[str]
    content: Optional[str]

class CommentSchema(BaseModel):
    post_id: str
    text: str
    author: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class CommentUpdateSchema(BaseModel):
    text: Optional[str]
