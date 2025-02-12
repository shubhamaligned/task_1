from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "blog"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
posts_collection = database["posts"]
comments_collection = database["comments"]
