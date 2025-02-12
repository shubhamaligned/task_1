from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from app.database import comments_collection, posts_collection
from app.schemas import CommentSchema, CommentUpdateSchema

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_comment(comment: CommentSchema):
    if not await posts_collection.find_one({"_id": ObjectId(comment.post_id)}):
        raise HTTPException(status_code=404, detail="Post not found")
    
    comment_dict = comment.dict()
    comment_dict["post_id"] = ObjectId(comment.post_id)  # Convert to ObjectId
    result = await comments_collection.insert_one(comment_dict)
    
    comment_dict["_id"] = str(result.inserted_id)
    comment_dict["post_id"] = str(comment_dict["post_id"])
    
    return comment_dict


@router.get("/{comment_id}")
async def get_comment(comment_id: str):
    comment = await comments_collection.find_one({"_id": ObjectId(comment_id)})
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment["_id"] = str(comment["_id"])
    comment["post_id"] = str(comment["post_id"])
    return comment

@router.put("/{comment_id}")
async def update_comment(comment_id: str, update_data: CommentUpdateSchema):
    update_dict = {k: v for k, v in update_data.dict().items() if v is not None}
    if not update_dict:
        raise HTTPException(status_code=400, detail="No valid fields to update")

    result = await comments_collection.update_one({"_id": ObjectId(comment_id)}, {"$set": update_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment updated successfully"}

@router.delete("/{comment_id}")
async def delete_comment(comment_id: str):
    result = await comments_collection.delete_one({"_id": ObjectId(comment_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted successfully"}
