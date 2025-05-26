# currency_bot/handlers/start.py

from aiogram import Router, F
from aiogram.types import Message
from services.user_service import save_user_language, get_user_language
from services.texts import texts
from keyboards.language import language_keyboard
from keyboards.menu_buttons import main_menu_keyboard

router = Router()

# 🇺🇿 🇷🇺 🇬🇧 til variantlari
LANG_OPTIONS = {
    "🇺🇿 O‘zbekcha": "uz",
    "🇷🇺 Русский": "ru",
    "🇬🇧 English": "en",
}


@router.message(F.text == "/start")
async def cmd_start(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)

    if lang in ("uz", "ru", "en"):
        # ✅ Til allaqachon tanlangan → to‘g‘ridan-to‘g‘ri menyu
        menu_text = texts["menu_select_service"].get(lang, texts["menu_select_service"]["en"])
        await message.answer(menu_text, reply_markup=main_menu_keyboard(lang))
    else:
        # 🆕 Yangi foydalanuvchi → til tanlash
        welcome = texts["start_welcome"].get("en", "👋 Welcome! Please select your language:")
        await message.answer(welcome, reply_markup=language_keyboard())


@router.message(F.text.in_(LANG_OPTIONS.keys()))
async def set_user_language(message: Message):
    user_id = message.from_user.id
    selected_text = message.text
    lang = LANG_OPTIONS.get(selected_text, "en")

    await save_user_language(user_id, lang)

    # ✅ Javoblar tanlangan tilga mos
    confirm = texts["language_saved"].get(lang, texts["language_saved"]["en"])
    menu_text = texts["menu_select_service"].get(lang, texts["menu_select_service"]["en"])

    await message.answer(confirm)
    await message.answer(menu_text, reply_markup=main_menu_keyboard(lang))
