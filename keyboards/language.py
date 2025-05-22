# currency_bot/keyboards/language.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def language_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="🇺🇿 O‘zbekcha")],
        [KeyboardButton(text="🇷🇺 Русский")],
        [KeyboardButton(text="🇬🇧 English")]
    ]

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )
