from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from config import DB_URL
MONGO_URI = "DB_URL"
mongo = MongoClient(MONGO_URI)
db = mongo["Client"]
