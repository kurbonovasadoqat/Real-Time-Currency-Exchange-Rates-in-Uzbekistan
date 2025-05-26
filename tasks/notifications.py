import logging
from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest
from services.exchange_service import get_cbu_rate
from services.user_service import (
    get_all_users_with_notifications_enabled,
    remove_user,
)


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

            except TelegramForbiddenError:
                logging.warning(f"⚠️ Bot foydalanuvchi tomonidan bloklangan: {user_id}")
                await remove_user(user_id)

            except TelegramBadRequest as e:
                logging.error(f"🚫 TelegramBadRequest: foydalanuvchi {user_id}, sabab: {e}")

            except Exception as e:
                logging.exception(f"❌ Kutilmagan xatolik: foydalanuvchi {user_id}, sabab: {e}")

    except Exception as e:
        logging.exception(f"🚨 Umumiy xatolik: {e}")
