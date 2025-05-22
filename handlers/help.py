# currency_bot/handlers/help.py

from aiogram import Router, F
from aiogram.types import Message
import logging

from services.texts import texts
from services.user_service import get_user_language
from keyboards.menu_buttons import main_menu_keyboard

router = Router()

HELP_BUTTONS = ["❓ Yordam", "❓ Помощь", "❓ Help"]

@router.message(F.text.in_(HELP_BUTTONS))
async def show_help(message: Message):
    user_id = message.from_user.id
    try:
        lang = await get_user_language(user_id)
        help_text = texts["help_text"].get(lang, texts["help_text"]["en"])
    except Exception:
        logging.exception("❌ Yordam matni olishda xatolik")
        help_text = texts["help_text"]["en"]

    await message.answer(help_text, reply_markup=main_menu_keyboard(lang))
