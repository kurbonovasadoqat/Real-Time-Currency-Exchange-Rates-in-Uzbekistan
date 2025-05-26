import os
from decimal import Decimal

# 🔍 DEBUG: ENV o'qilayaptimi tekshiradi (Logs'da ko'rinadi)
print("🔥 DEBUG - ENV OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# ✅ Foydali yordamchi funksiya
def _get_env(name: str, default=None, required=False):
    val = os.getenv(name, default)
    if required and val is None:
        raise EnvironmentError(f"❌ Required environment variable not found: {name}")
    return val

# 🔐 Telegram bot va MongoDB
BOT_TOKEN = _get_env("BOT_TOKEN", required=True)
MONGO_URI = _get_env("MONGO_URI", required=True)
MONGO_DB_NAME = _get_env("MONGO_DB_NAME", "currency_bot")

# 🧠 OpenAI
OPENAI_API_KEY = _get_env("OPENAI_API_KEY", required=True)

# 🌍 API kalitlar
FREECURRENCY_API_KEY = _get_env("FREECURRENCY_API_KEY", required=True)
FIXER_API_KEY = _get_env("FIXER_API_KEY", required=True)
CURRENCYLAYER_API_KEY = _get_env("CURRENCYLAYER_API_KEY", required=True)

# 📈 Valyuta manbalari
CBU_ARCHIVE_URL = _get_env("CBU_ARCHIVE_URL", "https://cbu.uz/oz/arkhiv-kursov-valyut/json/")
FOREX_API_URL = _get_env("FOREX_API_URL", "https://api.exchangerate.host/latest")

# ⚫ Qora bozor kurs koeffitsiyentlari
BLACK_MULTIPLIERS = {
    "USD": Decimal(_get_env("BLACK_MULT_USD", "1.115")),
    "EUR": Decimal(_get_env("BLACK_MULT_EUR", "1.10")),
    "RUB": Decimal(_get_env("BLACK_MULT_RUB", "1.08")),
}

# 🔁 Retry va cache
BACKOFF_MAX_TRIES = int(_get_env("BACKOFF_MAX_TRIES", 3))
CACHE_TTL_SECONDS = int(_get_env("CACHE_TTL_SECONDS", 300))

# ⏰ Har kunlik notification vaqti
DAILY_NOTIFICATION_TIME = _get_env("DAILY_NOTIFICATION_TIME", "09:00")

# 🪵 Log darajasi
LOG_LEVEL = _get_env("LOG_LEVEL", "INFO")
