from typing import List
from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from app.models import PostSchemaWithComments
from app.database import posts_collection
from app.schemas import PostSchema, PostUpdateSchema

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostSchema):
    post_dict = post.dict()
    result = await posts_collection.insert_one(post_dict)
    return {**post_dict, "_id": str(result.inserted_id)}

@router.get("/{post_id}")
async def get_post(post_id: str):
    post = await posts_collection.find_one({"_id": ObjectId(post_id)})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post["_id"] = str(post["_id"])
    return post

@router.get("/", response_model=List[PostSchemaWithComments])
async def get_posts(
    skip: int = 0,
    limit: int = 10,
    sort_by: str = "created_at",
    order: int = -1
):
    cursor = posts_collection.aggregate([
        {
            "$lookup": {
                "from": "comments",
                "localField": "_id",
                "foreignField": "post_id",
                "as": "comments"
            }
        },
        {"$sort": {sort_by: order}},  # Sort by created_at (or other field)
        {"$skip": skip},              # Pagination skip
        {"$limit": limit}             # Pagination limit
    ])
    
    posts = await cursor.to_list(length=limit)

    for post in posts:
        post["_id"] = str(post["_id"])
        for comment in post["comments"]:
            comment["_id"] = str(comment["_id"])
            comment["post_id"] = str(comment["post_id"])

    return posts

@router.put("/{post_id}")
async def update_post(post_id: str, update_data: PostUpdateSchema):
    update_dict = {k: v for k, v in update_data.dict().items() if v is not None}
    if not update_dict:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    result = await posts_collection.update_one({"_id": ObjectId(post_id)}, {"$set": update_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post updated successfully"}

@router.delete("/{post_id}")
async def delete_post(post_id: str):
    result = await posts_collection.delete_one({"_id": ObjectId(post_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
