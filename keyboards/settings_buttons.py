# currency_bot/keyboards/settings_buttons.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from typing import Dict

# 🌐 Har bir til uchun sozlamalar menyusidagi tugma matnlari
SETTINGS_LABELS: Dict[str, Dict[str, str]] = {
    "uz": {
        "language":   "🌐 Tilni o‘zgartirish",
        "notif_on":   "🔕 Bildirishnomani o‘chirish",
        "notif_off":  "🔔 Bildirishnomani yoqish",
        "back":       "⬅️ Asosiy menyuga qaytish",
    },
    "ru": {
        "language":   "🌐 Изменить язык",
        "notif_on":   "🔕 Отключить уведомления",
        "notif_off":  "🔔 Включить уведомления",
        "back":       "⬅️ Вернуться в меню",
    },
    "en": {
        "language":   "🌐 Change Language",
        "notif_on":   "🔕 Turn Off Notifications",
        "notif_off":  "🔔 Turn On Notifications",
        "back":       "⬅️ Back to Menu",
    },
}

def settings_keyboard(lang: str, notifications_enabled: bool = True) -> ReplyKeyboardMarkup:
    """
    Sozlamalar menyusiga mos klaviatura qaytaradi:
    - Foydalanuvchi tiliga qarab
    - Bildirishnoma holatiga qarab

    :param lang: 'uz', 'ru', 'en'
    :param notifications_enabled: True => "🔕 O‘chirish", False => "🔔 Yoqish"
    :return: ReplyKeyboardMarkup
    """
    labels = SETTINGS_LABELS.get(lang, SETTINGS_LABELS["en"])
    notif_button = labels["notif_on"] if notifications_enabled else labels["notif_off"]

    keyboard = [
        [KeyboardButton(text=labels["language"])],
        [KeyboardButton(text=notif_button)],
        [KeyboardButton(text=labels["back"])],
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        one_time_keyboard=False
    )
