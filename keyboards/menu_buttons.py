# currency_bot/keyboards/menu_buttons.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from typing import Dict, List

MENU_LAYOUT: Dict[str, List[List[str]]] = {
    "uz": [
        ["🏦 Markaziy Bank",      "⚫ Qora Bozor"],
        ["🌍 Xalqaro Kurslar",    "💱 Kripto valyutalar"],
        ["💱 Convert",            "⚙️ Sozlamalar"],
        ["❓ Yordam"],
    ],
    "ru": [
        ["🏦 Центральный Банк",   "⚫ Черный рынок"],
        ["🌍 Международные курсы", "💱 Криптовалюты"],
        ["💱 Конвертация",        "⚙️ Настройки"],
        ["❓ Помощь"],
    ],
    "en": [
        ["🏦 Central Bank",       "⚫ Black Market"],
        ["🌍 International Rates","💱 Crypto Prices"],
        ["💱 Convert",            "⚙️ Settings"],
        ["❓ Help"],
    ],
}

def main_menu_keyboard(lang: str) -> ReplyKeyboardMarkup:
    layout = MENU_LAYOUT.get(lang, MENU_LAYOUT["en"])
    keyboard = [
        [KeyboardButton(text=label) for label in row]
        for row in layout
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )
