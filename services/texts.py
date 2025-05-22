# currency_bot/services/texts.py

texts = {
    "start_welcome": {
        "uz": "👋 Assalomu alaykum! Bu bot orqali siz valyuta kurslarini bilib olasiz.\n\nIltimos, tilni tanlang:",
        "ru": "👋 Добро пожаловать! Этот бот показывает актуальные курсы валют.\n\nПожалуйста, выберите язык:",
        "en": "👋 Welcome! This bot provides real-time currency exchange rates.\n\nPlease select your language:",
    },
    "language_prompt": {
        "uz": "👇 Tilni tanlang:",
        "ru": "👇 Выберите язык:",
        "en": "👇 Choose your language:"
    },
    
    "language_saved": {
        "uz": "✅ Til saqlandi!",
        "ru": "✅ Язык сохранён!",
        "en": "✅ Language saved!",
    },
    "language_updated": {
        "uz": "✅ Til o‘zgartirildi.",
        "ru": "✅ Язык изменён.",
        "en": "✅ Language updated.",
    },
    "menu_select_service": {
        "uz": "📋 Xizmat turini tanlang:",
        "ru": "📋 Выберите услугу:",
        "en": "📋 Choose a service:",
    },
    "black_success": {
        "uz": "⚫ Qora bozor kurslari:\n\n🇺🇸 1 USD = {usd} so‘m\n🇪🇺 1 EUR = {eur} so‘m\n🇷🇺 1 RUB = {rub} so‘m",
        "ru": "⚫ Курсы черного рынка:\n\n🇺🇸 1 USD = {usd} сум\n🇪🇺 1 EUR = {eur} сум\n🇷🇺 1 RUB = {rub} сум",
        "en": "⚫ Black Market Rates:\n\n🇺🇸 1 USD = {usd} UZS\n🇪🇺 1 EUR = {eur} UZS\n🇷🇺 1 RUB = {rub} UZS",
    },
    "black_error": {
        "uz": "❌ Qora bozor kursini olishda xatolik yuz berdi.",
        "ru": "❌ Ошибка при получении курса черного рынка.",
        "en": "❌ Failed to fetch black market rate.",
    },
    "international_multi": {
        "uz": "🌍 Xalqaro kurslar:\n\n🇺🇸 1 USD ➔ {uzs} so‘m\n🇪🇺 1 USD ➔ {eur} yevro\n🇷🇺 1 USD ➔ {rub} rubl",
        "ru": "🌍 Международные курсы:\n\n🇺🇸 1 USD ➔ {uzs} сум\n🇪🇺 1 USD ➔ {eur} евро\n🇷🇺 1 USD ➔ {rub} рубль",
        "en": "🌍 International Rates:\n\n🇺🇸 1 USD ➔ {uzs} UZS\n🇪🇺 1 USD ➔ {eur} EUR\n🇷🇺 1 USD ➔ {rub} RUB",
    },

    "international_error": {
        "uz": "❌ Xalqaro kurslarni olishda xatolik yuz berdi.",
        "ru": "❌ Ошибка получения международных курсов.",
        "en": "❌ Failed to fetch international rates.",
    },
    "crypto_success": {
        "uz": "🌐 Kripto kurslari:\n\n₿ 1 BTC = {btc} USDT\nΞ 1 ETH = {eth} USDT",
        "ru": "🌐 Курсы криптовалют:\n\n₿ 1 BTC = {btc} USDT\nΞ 1 ETH = {eth} USDT",
        "en": "🌐 Crypto Prices:\n\n₿ 1 BTC = {btc} USDT\nΞ 1 ETH = {eth} USDT"
    },
    "crypto_error": {
        "uz": "❌ Kripto narxlarini olishda xatolik yuz berdi.",
        "ru": "❌ Ошибка при получении курсов криптовалют.",
        "en": "❌ Failed to fetch crypto prices.",
    },
    "cbu_success": {
        "uz": "🏦 Markaziy Bank kurslari:\n\n🇺🇸 1 USD = {usd} so‘m\n🇪🇺 1 EUR = {eur} so‘m\n🇷🇺 1 RUB = {rub} so‘m",
        "ru": "🏦 Курсы Центрального Банка:\n\n🇺🇸 1 USD = {usd} сум\n🇪🇺 1 EUR = {eur} сум\n🇷🇺 1 RUB = {rub} сум",
        "en": "🏦 Central Bank Rates:\n\n🇺🇸 1 USD = {usd} UZS\n🇪🇺 1 EUR = {eur} UZS\n🇷🇺 1 RUB = {rub} UZS",
    },
    "cbu_error": {
        "uz": "❌ Markaziy Bank kurslarini olishda xatolik yuz berdi.",
        "ru": "❌ Ошибка при получении курсов Центрального Банка.",
        "en": "❌ Failed to fetch Central Bank rates.",
},

    # ✅ HELP
    "help_text": {
        "uz": (
            "🆘 <b>Yordam</b>\n\n"
            "Quyidagi xizmatlardan foydalanishingiz mumkin:\n"
            "• 🏦 Markaziy Bank kurslari\n"
            "• ⚫ Qora Bozor kurslari\n"
            "• 🌍 Xalqaro kurslar\n"
            "• 💱 Kripto narxlari (BTC, ETH)\n\n"
            "Tilni o‘zgartirish uchun ⚙️ Sozlamalar menyusiga kiring"
        ),
        "ru": (
            "🆘 <b>Помощь</b>\n\n"
            "Вы можете использовать следующие функции:\n"
            "• 🏦 Курсы Центрального Банка\n"
            "• ⚫ Курсы черного рынка\n"
            "• 🌍 Международные курсы\n"
            "• 💱 Криптовалюты (BTC, ETH)\n\n"
            "Чтобы изменить язык, перейдите в ⚙️ Настройки"
        ),
        "en": (
            "🆘 <b>Help</b>\n\n"
            "Available features:\n"
            "• 🏦 Central Bank rates\n"
            "• ⚫ Black Market rates\n"
            "• 🌍 International rates\n"
            "• 💱 Crypto prices (BTC, ETH)\n\n"
            "To change language, go to ⚙️ Settings"
        ),
    },

    # ❌ ERRORS
    "conversion_error": {
        "uz": "❌ Konvertatsiyada xatolik yuz berdi.",
        "ru": "❌ Ошибка при конвертации.",
        "en": "❌ Conversion error.",
    },
    "ai_error": {
        "uz": "🤖 AI matnni tushunolmadi. Formatni tekshiring.",
        "ru": "🤖 AI не понял запрос. Проверьте формат.",
        "en": "🤖 AI couldn't understand. Check the format.",
    },
    "not_found": {
        "uz": "❗ Valyutani aniqlay olmadim.",
        "ru": "❗ Не удалось определить валюту.",
        "en": "❗ Couldn't detect currency.",
    },
    "black_error": {
        "uz": "❌ Qora bozor kursini olishda xatolik.",
        "ru": "❌ Ошибка при получении черного курса.",
        "en": "❌ Failed to get black market rate.",
    },
    "cbu_error": {
        "uz": "❌ Markaziy Bank kursini olishda xatolik.",
        "ru": "❌ Ошибка при получении курса ЦБ.",
        "en": "❌ Failed to get CBU rate.",
    },
    "settings_menu": {
    "uz": "⚙️ Sozlamalar menyusidan birini tanlang:",
    "ru": "⚙️ Выберите параметр настройки:",
    "en": "⚙️ Choose from the settings menu:"
},
"notifications_enabled": {
    "uz": "🔔 Bildirishnomalar yoqildi.",
    "ru": "🔔 Уведомления включены.",
    "en": "🔔 Notifications enabled.",
},
"notifications_disabled": {
    "uz": "🔕 Bildirishnomalar o‘chirildi.",
    "ru": "🔕 Уведомления отключены.",
    "en": "🔕 Notifications disabled.",
},
"back_to_menu": {
    "uz": "⬅️ Asosiy menyuga qaytdingiz.",
    "ru": "⬅️ Вы вернулись в главное меню.",
    "en": "⬅️ Returned to main menu.",
},


    # ✅ RESULT
    "realtime_result": {
        "uz": (
            "💱 {amount:,} {from_currency} → {to_currency}\n\n"
            "🧠 <b>Real vaqtli kurs:</b>\n"
            "<b>{converted:,.2f} {to_currency}</b>\n"
            "📈 1 {from_currency} = {rate:,.4f} {to_currency}"
        ),
        "ru": (
            "💱 {amount:,} {from_currency} → {to_currency}\n\n"
            "🧠 <b>Курс в реальном времени:</b>\n"
            "<b>{converted:,.2f} {to_currency}</b>\n"
            "📈 1 {from_currency} = {rate:,.4f} {to_currency}"
        ),
        "en": (
            "💱 {amount:,} {from_currency} → {to_currency}\n\n"
            "🧠 <b>Real-time rate:</b>\n"
            "<b>{converted:,.2f} {to_currency}</b>\n"
            "📈 1 {from_currency} = {rate:,.4f} {to_currency}"
        ),
    },

    # ⚙️ SETTINGS
    "settings_menu": {
        "uz": "⚙️ Sozlamalar menyusidan birini tanlang:",
        "ru": "⚙️ Выберите параметр настройки:",
        "en": "⚙️ Choose from the settings menu:",
    },
    "notifications_enabled": {
        "uz": "🔔 Bildirishnomalar yoqildi.",
        "ru": "🔔 Уведомления включены.",
        "en": "🔔 Notifications enabled.",
    },
    "notifications_disabled": {
        "uz": "🔕 Bildirishnomalar o‘chirildi.",
        "ru": "🔕 Уведомления отключены.",
        "en": "🔕 Notifications disabled.",
    },
    "back_to_menu": {
        "uz": "⬅️ Asosiy menyuga qaytdingiz.",
        "ru": "⬅️ Вы вернулись в главное меню.",
        "en": "⬅️ Returned to main menu.",
    },
}
