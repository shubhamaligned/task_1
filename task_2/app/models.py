from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CommentSchema(BaseModel):
    _id: Optional[str]
    text: str
    created_at: datetime

class PostSchemaWithComments(BaseModel):
    _id: Optional[str]
    title: str
    content: str
    author: str
    created_at: datetime
    comments: List[CommentSchema] 