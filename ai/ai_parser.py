import json
from ai.openai_client import chat_completion


async def extract_conversion_info(user_text: str, lang: str = "en", mode: str = "soft") -> dict:
    """
    AI yordamida foydalanuvchi matnidan valyuta miqdori va kodlarini ajratib olish.

    :param user_text: Foydalanuvchi yuborgan matn
    :param lang: 'uz', 'ru', 'en'
    :param mode: 'soft' (default) yoki 'strict'
    :return: {amount: float, from_currency: str, to_currency: str}
    """

    if mode == "strict":
        prompt = f"""
You are a precise currency parser bot.

Your job is to extract EXACTLY 3 fields from user input:
- "amount": (a number)
- "from_currency": (3-letter ISO currency code)
- "to_currency": (3-letter ISO currency code)

Only return valid JSON, like:
{{ "amount": 100, "from_currency": "USD", "to_currency": "UZS" }}

No explanation. If format is wrong, leave fields empty.

User language: {lang}
User input: "{user_text}"
"""
    else:
        # SOFT – fallback bo‘ladi
        prompt = f"""
You are a helpful assistant for currency conversion.

Extract 3 fields:
- amount
- from_currency
- to_currency

💡 Recognize synonyms, country-based references, slang and symbols:
- USD → "usd", "dollar", "$", "amerika dollari", "доллар"
- UZS → "uz", "so'm", "som", "uzs", "sum", "uzbek money"
- EUR → "euro", "evro", "yevro", "eur", "€"
- RUB → "rub", "rubl", "рубль"
- BTC → "btc", "bitcoin", "₿"
- ETH → "eth", "ethereum"
- USDT → "usdt", "tether", "tether coin", "usdt token"
- CNY, JPY, INR, TRY, KRW, KZT, GBP, CHF, AED... etc.

🌐 Language: {lang}
🧾 User Input: "{user_text}"

If amount is missing, assume amount = 1.

Return only JSON:
{{ "amount": 1, "from_currency": "BTC", "to_currency": "UZS" }}
"""

    try:
        response = await chat_completion(prompt)
        parsed = json.loads(response)

        # Fallback: agar soft mode bo‘lsa va amount yo‘q bo‘lsa → 1
        if mode == "soft" and (
            parsed.get("amount") is None and parsed.get("from_currency") and parsed.get("to_currency")
        ):
            parsed["amount"] = 1.0

        return parsed

    except json.JSONDecodeError as e:
        print("❌ JSON parsing xatoligi:", e)
        print("📥 AI javobi:", response)
        return {}

    except Exception as e:
        print("❌ AI parsing umumiy xatolik:", e)
        return {}
