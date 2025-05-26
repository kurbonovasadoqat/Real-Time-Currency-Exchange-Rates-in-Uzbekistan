import logging
from aiohttp import ClientSession
from decimal import Decimal
from typing import Dict, Optional
from aiocache import cached, Cache

from services.texts import texts

# 🔗 API manzili
BLACK_MARKET_API = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"

# 🌐 Global sessiya
_session: Optional[ClientSession] = None


async def get_client_session() -> ClientSession:
    """
    ClientSession ni global holatda qayta ishlatish.
    """
    global _session
    if _session is None or _session.closed:
        _session = ClientSession()
    return _session


@cached(ttl=300, cache=Cache.MEMORY)
async def get_blackmarket_rates(lang: str = "en") -> str:
    """
    Qora bozor kurslarini olish — CBU arxiv asosida.
    """
    try:
        session = await get_client_session()
        async with session.get(BLACK_MARKET_API) as response:
            data = await response.json()

        rates: Dict[str, Decimal] = {
            item["Ccy"]: Decimal(item.get("Rate", "0"))
            for item in data
        }
        usd = rates.get("USD", Decimal("0")) * Decimal("1.115")
        eur = rates.get("EUR", Decimal("0")) * Decimal("1.10")
        rub = rates.get("RUB", Decimal("0")) * Decimal("1.08")

        tmpl = texts["black_success"].get(lang, texts["black_success"]["en"])
        return tmpl.format(usd=f"{usd:,.0f}", eur=f"{eur:,.0f}", rub=f"{rub:,.0f}")

    except Exception:
        logging.exception("❌ Failed to fetch black market rates")
        return texts["black_error"].get(lang, texts["black_error"]["en"])


async def close_session() -> None:
    """
    Bot tugaganda ClientSession ni yopish.
    """
    global _session
    if _session and not _session.closed:
        await _session.close()
