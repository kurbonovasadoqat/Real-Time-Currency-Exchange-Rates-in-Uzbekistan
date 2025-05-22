# currency_bot/handlers/settings.py

from aiogram import Router, F
from aiogram.types import Message

from services.texts import texts
from services.user_service import (
    get_user_language,
    save_user_language,
    toggle_notifications,
    get_notification_status,
)
from keyboards.settings_buttons import settings_keyboard
from keyboards.language import language_keyboard
from keyboards.menu_buttons import main_menu_keyboard

router = Router()

# === Tugmalar matnlari (aniq moslik uchun) ===
SETTINGS_BUTTONS = [
    "⚙️ Sozlamalar", "⚙️ Настройки", "⚙️ Settings"
]

CHANGE_LANG_BUTTONS = [
    "🌐 Tilni o‘zgartirish", "🌐 Изменить язык", "🌐 Change Language"
]

LANGUAGE_OPTIONS = [
    "🇺🇿 O‘zbekcha", "🇷🇺 Русский", "🇬🇧 English"
]

TOGGLE_NOTIF_BUTTONS = [
    "🔕 Bildirishnomani o‘chirish", "🔔 Bildirishnomani yoqish",
    "🔕 Отключить уведомления", "🔔 Включить уведомления",
    "🔕 Turn Off Notifications", "🔔 Turn On Notifications"
]

BACK_BUTTONS = [
    "⬅️ Asosiy menyuga qaytish",
    "⬅️ Вернуться в меню",
    "⬅️ Back to Menu"
]


# === 1. Sozlamalar menyusini ko‘rsatish ===
@router.message(F.text.in_(SETTINGS_BUTTONS))
async def show_settings(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    status = await get_notification_status(user_id)
    text = texts.get("settings_menu", {}).get(lang, texts["settings_menu"]["en"])
    await message.answer(text, reply_markup=settings_keyboard(lang, status))

# === 2. Tilni o‘zgartirish bo‘limini chiqarish ===
@router.message(F.text.in_(CHANGE_LANG_BUTTONS))
async def show_language_options(message: Message):
    lang = await get_user_language(message.from_user.id)
    prompt = texts.get("language_prompt", {}).get(lang, texts["language_prompt"]["en"])
    await message.answer(prompt, reply_markup=language_keyboard())

# === 3. Foydalanuvchi yangi til tanlaganda ===
@router.message(F.text.in_(LANGUAGE_OPTIONS))
async def set_language(message: Message):
    lang_map = {
        "🇺🇿 O‘zbekcha": "uz",
        "🇷🇺 Русский": "ru",
        "🇬🇧 English": "en",
    }
    selected = lang_map.get(message.text.strip(), "en")
    await save_user_language(message.from_user.id, selected)

    confirmation = texts.get("language_saved", {}).get(selected, texts["language_saved"]["en"])
    menu_text = texts.get("menu_select_service", {}).get(selected, texts["menu_select_service"]["en"])
    await message.answer(confirmation)
    await message.answer(menu_text, reply_markup=main_menu_keyboard(selected))

# === 4. Bildirishnomani yoqish/o‘chirish ===
@router.message(F.text.in_(TOGGLE_NOTIF_BUTTONS))
async def toggle_notifications_handler(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    new_status = await toggle_notifications(user_id)
    key = "notifications_enabled" if new_status else "notifications_disabled"
    notif_text = texts.get(key, {}).get(lang, texts[key]["en"])
    await message.answer(notif_text, reply_markup=settings_keyboard(lang, new_status))

# === 5. Asosiy menyuga qaytish ===
@router.message(F.text.in_(BACK_BUTTONS))
async def back_to_menu(message: Message):
    lang = await get_user_language(message.from_user.id)
    text = texts.get("back_to_menu", {}).get(lang, texts["back_to_menu"]["en"])
    await message.answer(text, reply_markup=main_menu_keyboard(lang))
