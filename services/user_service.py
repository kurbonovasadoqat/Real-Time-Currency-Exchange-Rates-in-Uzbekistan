# currency_bot/services/user_service.py

import logging
from typing import Optional, AsyncIterator
from pymongo.errors import PyMongoError

from database.mongodb import get_collection

# MongoDB collection
users = get_collection("users")

# 🌐 Tilni saqlash
async def save_user_language(user_id: int, lang: str) -> None:
    try:
        await users.update_one(
            {"user_id": user_id},
            {"$set": {"language": lang, "notifications": True}},
            upsert=True
        )
    except PyMongoError:
        logging.exception("❌ Tilni saqlashda xatolik (user_id: %s)", user_id)


# 🌐 Tilni olish
async def get_user_language(user_id: int) -> str:
    try:
        user = await users.find_one({"user_id": user_id}, {"language": 1})
        return user.get("language", "en") if user else "en"
    except PyMongoError:
        logging.exception("❌ Tilni olishda xatolik (user_id: %s)", user_id)
        return "en"


# 🔔 Bildirishnoma holatini olish
async def get_notification_status(user_id: int) -> bool:
    try:
        user = await users.find_one({"user_id": user_id}, {"notifications": 1})
        return user.get("notifications", True) if user else True
    except PyMongoError:
        logging.exception("❌ Bildirishnoma holatini olishda xatolik")
        return True


# 🔁 Bildirishnomani almashtirish (yoqish/o‘chirish)
async def toggle_notifications(user_id: int) -> bool:
    try:
        user = await users.find_one({"user_id": user_id}, {"notifications": 1})
        current = user.get("notifications", True) if user else True
        new_status = not current
        await users.update_one(
            {"user_id": user_id},
            {"$set": {"notifications": new_status}},
            upsert=True
        )
        return new_status
    except PyMongoError:
        logging.exception("❌ Bildirishnomani o‘zgartirishda xatolik")
        return True


# 📤 Har kuni yuboriladiganlar
async def get_all_users_with_notifications_enabled() -> AsyncIterator[dict]:
    try:
        cursor = users.find({"notifications": True})
        async for user in cursor:
            yield user
    except PyMongoError:
        logging.exception("❌ Notifikatsiyaga ega foydalanuvchilarni olishda xatolik")
