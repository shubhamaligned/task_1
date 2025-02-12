from fastapi import FastAPI
from app.routes import posts, comments

app = FastAPI(title="Simple Blog API", description="A blog API with FastAPI & MongoDB")

app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(comments.router, prefix="/comments", tags=["Comments"])
