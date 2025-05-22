from aiogram import Router, F
from aiogram.types import Message
from services.user_service import get_user_language
from services.texts import texts
from services.fallback_manager import get_best_conversion
from ai.ai_parser import extract_conversion_info

router = Router()

# 🔒 Tugma matnlarini AI parsingdan chiqarib tashlash
IGNORE_TEXTS = {
    # Uzbek
    "🏦 Markaziy Bank", "⚫ Qora Bozor", "🌍 Xalqaro Kurslar", "💱 Kripto valyutalar",
    "💱 Convert", "⚙️ Sozlamalar", "🌐 Tilni o‘zgartirish",
    "🔕 Bildirishnomani o‘chirish", "🔔 Bildirishnomani yoqish",
    "⬅️ Asosiy menyuga qaytish", "❓ Yordam",
    "🇺🇿 O‘zbekcha", "🇷🇺 Русский", "🇬🇧 English",

    # Russian
    "🏦 Центральный Банк", "⚫ Черный рынок", "🌍 Международные курсы", "💱 Криптовалюты",
    "💱 Конвертация", "⚙️ Настройки", "🌐 Изменить язык",
    "🔕 Отключить уведомления", "🔔 Включить уведомления",
    "⬅️ Вернуться в меню", "❓ Помощь",

    # English
    "🏦 Central Bank", "⚫ Black Market", "🌍 International Rates", "💱 Crypto Prices",
    "💱 Convert", "⚙️ Settings", "🌐 Change Language",
    "🔕 Turn Off Notifications", "🔔 Turn On Notifications",
    "⬅️ Back to Menu", "❓ Help"
}


# 🔁 1. Convert tugmasi bosilganda misol so‘rov
@router.message(F.text.in_({
    "💱 Convert", "💱 Конвертация", "💱 Конвертировать"
}))
async def prompt_conversion(message: Message):
    lang = await get_user_language(message.from_user.id)

    prompt_text = {
        "uz": "💬 Iltimos, summani va valyutalarni kiriting (masalan: 100 USD dan UZS ga)",
        "ru": "💬 Введите сумму и валюты (например: 100 USD в UZS)",
        "en": "💬 Please enter amount and currencies (e.g. 100 USD to UZS)"
    }.get(lang, "💬 Please enter conversion request.")

    await message.answer(prompt_text)


# 🧠 2. Foydalanuvchi matn yuborganida konvertatsiya qilish
@router.message(F.text & ~F.text.in_(IGNORE_TEXTS))
async def convert_handler(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    text = message.text.strip()

    # 2️⃣ Bo‘sh yoki juda qisqa matn
    if not text or len(text) < 3:
        empty_warn = {
            "uz": "⚠️ Iltimos, miqdor va valyutalarni yozing.",
            "ru": "⚠️ Пожалуйста, введите сумму и валюты.",
            "en": "⚠️ Please enter amount and currencies."
        }.get(lang, "⚠️ Please enter amount and currencies.")
        return await message.answer(empty_warn)

    try:
        # 3️⃣ AI yordamida tahlil qilish
        parsed = await extract_conversion_info(text, lang)
        amount = parsed.get("amount")
        from_cur = parsed.get("from_currency")
        to_cur = parsed.get("to_currency")

        # 4️⃣ AI parsingda xatolik (format noto‘g‘ri)
        if not all([amount, from_cur, to_cur]):
            format_err = {
                "uz": "🤖 Format noto‘g‘ri. Masalan: <b>100 USD dan UZS ga</b>",
                "ru": "🤖 Неверный формат. Пример: <b>100 USD в UZS</b>",
                "en": "🤖 Invalid format. Example: <b>100 USD to UZS</b>"
            }.get(lang, "🤖 Invalid format.")
            return await message.answer(format_err)

        # 5️⃣ Eng yaxshi kursni olish (API orqali)
        try:
            result = await get_best_conversion(amount, from_cur, to_cur)
        except Exception as api_error:
            print("🔌 API xatolik:", api_error)
            api_fail = {
                "uz": "🔌 Kursni olishda xatolik yuz berdi.",
                "ru": "🔌 Ошибка при получении курса.",
                "en": "🔌 Failed to retrieve exchange rate."
            }.get(lang, "🔌 Conversion error.")
            return await message.answer(api_fail)

        # 6️⃣ Natijani chiqarish
        reply = texts["realtime_result"][lang].format(
            amount=amount,
            from_currency=from_cur,
            to_currency=to_cur,
            converted=result["converted"],
            rate=result["rate"]
        )
        await message.answer(reply)

    except Exception as e:
        print(f"❌ Umumiy konvertatsiya xatosi: {e}")
        unknown_error = texts.get("conversion_error", {}).get(lang, texts["conversion_error"]["en"])
        await message.answer(unknown_error)
