# currency_bot/main.py

import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import BOT_TOKEN, LOG_LEVEL, DAILY_NOTIFICATION_TIME
from logger import setup_logger

# ✅ Logger sozlash
setup_logger(LOG_LEVEL)
logger = logging.getLogger("currency_bot.main")

# 🔽 Router va boshqa importlar (logger'dan keyin bo‘lishi mumkin)
from handlers import (
    start,
    convert,
    market,
    help as help_menu,
    settings
)
from tasks.notifications import send_daily_cbu_notifications
from services.blackmarket_service import close_session as close_blackmarket_session


async def main():
    logger.info("🚀 Bot initialize qilinmoqda...")

    # 1. Bot va Dispatcher
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())
    logger.info("🤖 Bot va Dispatcher tayyor")

    # 2. Routerlarni ulash
    dp.include_router(start.router)
    dp.include_router(convert.router)
    dp.include_router(market.router)
    dp.include_router(help_menu.router)
    dp.include_router(settings.router)
    logger.info("🔗 Barcha routerlar ulandi")

    # 3. Scheduler — CBU xabarlari
    hour, minute = map(int, DAILY_NOTIFICATION_TIME.split(":"))
    scheduler = AsyncIOScheduler(timezone="Asia/Tashkent")

    # ✅ Har kuni 09:00 da yuboriladigan CBU xabari
    scheduler.add_job(
        send_daily_cbu_notifications,
        trigger="cron",
        hour=hour,
        minute=minute,
        args=[bot],
        id="daily_cbu_notifications"
    )
    logger.info(f"📅 CBU xabarlari har kuni {hour:02d}:{minute:02d} da yuboriladi.")

    # # ✅ TEST rejim: har 1 daqiqada yuboriladi
    # scheduler.add_job(
    #     send_daily_cbu_notifications,
    #     trigger="interval",
    #     minutes=1,
    #     args=[bot],
    #     id="test_cbu_every_minute"
    # )
    # logger.info("🧪 [TEST] Har 1 daqiqada CBU xabari yuborilishi yo‘lga qo‘yildi.")

    scheduler.start()

    # 4. Polling boshlash
    logger.info("✅ Bot tayyor. Polling boshlanmoqda...")
    try:
        await dp.start_polling(bot)
    finally:
        logger.info("🛑 Bot to‘xtatilyapti, tozalash ishlari...")
        scheduler.shutdown()
        await bot.session.close()
        await close_blackmarket_session()
        logger.info("✅ Bot to‘xtatildi. Barcha resurslar tozalandi.")


if __name__ == "__main__":
    asyncio.run(main())
