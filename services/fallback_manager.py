# currency_bot/services/fallback_manager.py

from typing import Optional
from providers.fca_provider import FreeCurrencyAPIProvider
from providers.fixer_provider import FixerAPIProvider
from providers.currencylayer_provider import CurrencyLayerProvider

# Ketma-ket sinab ko‘riladigan providerlar
PROVIDERS = [
    FreeCurrencyAPIProvider(),
    FixerAPIProvider(),
    CurrencyLayerProvider(),
]

async def get_best_rate(from_cur: str, to_cur: str) -> Optional[float]:
    for provider in PROVIDERS:
        try:
            rate = await provider.get_rate(from_cur, to_cur)
            if rate:
                return rate
        except Exception:
            continue
    return None


async def get_best_conversion(amount: float, from_cur: str, to_cur: str) -> dict:
    rate = await get_best_rate(from_cur, to_cur)
    if rate is None:
        raise RuntimeError("❌ Hech bir provayderdan kurs olinmadi.")
    return {
        "rate": rate,
        "converted": round(rate * amount, 2)
    }
