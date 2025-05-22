# currency_bot/tasks/notifications.py

import logging
from aiogram import Bot
from services.exchange_service import get_cbu_rate
from services.user_service import get_all_users_with_notifications_enabled

async def send_daily_cbu_notifications(bot: Bot) -> None:
    """
    Har kuni ertalab Markaziy Bank kurslarini yuboradi.
    Faqat bildirishnomasi yoqilgan foydalanuvchilarga.
    """
    logging.info("📤 Daily CBU notification boshlanyapti...")

    try:
        async for user in get_all_users_with_notifications_enabled():
            user_id = user.get("user_id")
            lang = user.get("language", "en")

            try:
                text = await get_cbu_rate(lang)
                await bot.send_message(chat_id=user_id, text=text)
                logging.info(f"✅ CBU yuborildi: {user_id} ({lang})")

            except Exception as e:
                logging.exception(f"❌ Xatolik: foydalanuvchi {user_id}, sabab: {e}")

    except Exception as e:
        logging.exception(f"🚨 Umumiy xatolik: {e}")
