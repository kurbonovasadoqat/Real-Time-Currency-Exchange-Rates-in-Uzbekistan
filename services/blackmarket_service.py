# currency_bot/services/blackmarket_service.py

import logging
from aiohttp import ClientSession, ClientError
from decimal import Decimal
from typing import Any, Dict, Optional
import backoff
from aiocache import cached, Cache

from services.texts import texts
from config import CBU_ARCHIVE_URL, BLACK_MULTIPLIERS, CACHE_TTL_SECONDS

# 🧪 Monitoring uchun (ixtiyoriy, istasangiz o‘chirib qo‘yishingiz mumkin)
from prometheus_client import Counter

BLACK_REQ = Counter("blackmarket_requests_total", "Total black market requests")
BLACK_FAIL = Counter("blackmarket_failures_total", "Black market request failures")

# 🌐 Bitta sessiya (performance uchun)
_session: Optional[ClientSession] = None


async def get_client_session() -> ClientSession:
    global _session
    if _session is None or _session.closed:
        _session = ClientSession()
    return _session


@backoff.on_exception(backoff.expo, (ClientError,), max_tries=3, jitter=backoff.full_jitter)
async def fetch_data(session: ClientSession, url: str) -> Any:
    """
    Retry bilan JSON ma’lumotlarni olish (CBU API)
    """
    async with session.get(url, timeout=10) as response:
        response.raise_for_status()
        return await response.json()


@cached(ttl=CACHE_TTL_SECONDS, cache=Cache.MEMORY)
async def get_blackmarket_rates(lang: str = "en") -> str:
    """
    Qora bozor kurslarini CBU asosida multiplikator bilan hisoblab, formatlab qaytaradi
    """
    BLACK_REQ.inc()
    try:
        session = await get_client_session()
        data = await fetch_data(session, CBU_ARCHIVE_URL)

        # CBU valyuta kurslarini dict holatda olish
        rates: Dict[str, Decimal] = {
            item["Ccy"]: Decimal(item.get("Rate", "0"))
            for item in data
        }

        # Multiplikatorlar asosida qora bozor kurslarini hisoblash
        results: Dict[str, Decimal] = {}
        for cur, multiplier in BLACK_MULTIPLIERS.items():
            base = rates.get(cur, Decimal("0"))
            results[cur.lower()] = base * multiplier

        # Formatlash
        template = texts["black_success"].get(lang, texts["black_success"]["en"])
        formatted = {k: f"{v:,.2f}" for k, v in results.items()}
        return template.format(**formatted)

    except Exception as e:
        BLACK_FAIL.inc()
        logging.exception("Qora bozor kursini olishda xatolik: %s", e)
        return texts["black_error"].get(lang, texts["black_error"]["en"])


async def close_session() -> None:
    """
    Bot to‘xtaganda HTTP sessiyani toza yopish
    """
    global _session
    if _session and not _session.closed:
        await _session.close()
