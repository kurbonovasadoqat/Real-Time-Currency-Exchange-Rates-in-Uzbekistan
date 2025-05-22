# currency_bot/main.py

import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import BOT_TOKEN, LOG_LEVEL, DAILY_NOTIFICATION_TIME
from logger import setup_logger
from handlers import (
    start,
    convert,
    market,
    help as help_menu,
    settings
)
from tasks.notifications import send_daily_cbu_notifications
from services.blackmarket_service import close_session as close_blackmarket_session

# 0. Logger sozlash — dastlab bir marta chaqiriladi
setup_logger(LOG_LEVEL)

async def main():
    # 1. TEST SIGNAL
    print("🟢 [main.py] Bot ishga tushmoqda...")

    logging.info("🚀 Bot initialize qilinmoqda...")

    # 2. Bot va Dispatcher
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    # 3. Routerlar
    dp.include_router(start.router)
    dp.include_router(convert.router)
    dp.include_router(market.router)
    dp.include_router(help_menu.router)
    dp.include_router(settings.router)

    # 4. Scheduler — CBU kurslarini yuborish (kuniga 1 marta)
    try:
        hour, minute = map(int, DAILY_NOTIFICATION_TIME.split(":"))
        scheduler = AsyncIOScheduler(timezone="Asia/Tashkent")
        scheduler.add_job(
            send_daily_cbu_notifications,
            trigger="cron",
            hour=hour,
            minute=minute,
            args=[bot],
            id="daily_cbu_notifications"
        )
        scheduler.start()
        logging.info(f"⏰ Kunlik CBU xabarlari: {hour:02d}:{minute:02d} da yuboriladi")
    except Exception as e:
        logging.warning(f"⚠️ Scheduler ishga tushmadi: {e}")

    # 5. Polling
    logging.info("🤖 Bot ishga tushdi. Polling boshlanmoqda...")
    try:
        await dp.start_polling(bot)
    finally:
        # 6. Tozalash
        logging.info("🛑 Bot to‘xtatilyapti...")
        scheduler.shutdown()
        await bot.session.close()
        await close_blackmarket_session()
        logging.info("✅ Tozalash tugadi. Bot yopildi.")


if __name__ == "__main__":
    asyncio.run(main())
