# ✅ CACHED EXCHANGE SERVICE
# currency_bot/services/exchange_service.py

import logging
from aiohttp import ClientSession
from decimal import Decimal
from typing import Dict
from aiocache import cached, Cache
from services.texts import texts

CBU_API = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
OPEN_API = "https://open.er-api.com/v6/latest/USD"

@cached(ttl=300, cache=Cache.MEMORY)
async def get_cbu_rate(lang: str = "en") -> str:
    try:
        async with ClientSession() as session:
            async with session.get(CBU_API) as response:
                data = await response.json()

        rates: Dict[str, Decimal] = {
            item["Ccy"]: Decimal(item.get("Rate", "0"))
            for item in data
        }
        usd = rates.get("USD", Decimal("0"))
        eur = rates.get("EUR", Decimal("0"))
        rub = rates.get("RUB", Decimal("0"))

        tmpl = texts["cbu_success"].get(lang, texts["cbu_success"]["en"])
        return tmpl.format(usd=f"{usd:,.2f}", eur=f"{eur:,.2f}", rub=f"{rub:,.2f}")

    except Exception:
        logging.exception("Failed to fetch CBU rate")
        return texts["cbu_error"].get(lang, texts["cbu_error"]["en"])


@cached(ttl=300, cache=Cache.MEMORY)
async def get_international_rate(lang: str = "en") -> str:
    try:
        async with ClientSession() as session:
            async with session.get(OPEN_API) as response:
                data = await response.json()

        rates = data.get("rates", {})
        uzs = Decimal(str(rates.get("UZS", 0)))
        eur = Decimal(str(rates.get("EUR", 0)))
        rub = Decimal(str(rates.get("RUB", 0)))

        tmpl = texts["international_multi"].get(lang, texts["international_multi"]["en"])
        return tmpl.format(uzs=f"{uzs:,.2f}", eur=f"{eur:.2f}", rub=f"{rub:.2f}")

    except Exception:
        logging.exception("Failed to fetch international rates")
        return texts["international_error"].get(lang, texts["international_error"]["en"])
