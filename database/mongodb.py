# currency_bot/database/mongodb.py

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from typing import Optional
import logging
import os

from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "currency_bot")

_client: Optional[AsyncIOMotorClient] = None


def get_client() -> AsyncIOMotorClient:
    global _client
    if _client is None:
        if not MONGO_URI:
            raise ValueError("❌ MONGO_URI topilmadi (.env faylga qo‘shing)")
        _client = AsyncIOMotorClient(MONGO_URI)
        logging.info("✅ MongoDB client yaratildi")
    return _client


def get_db() -> AsyncIOMotorDatabase:
    return get_client()[MONGO_DB_NAME]


def get_collection(name: str):
    return get_db()[name]

client = AsyncIOMotorClient(MONGO_URI)
db = client["currency_db"]
users_collection = db["users"] 
