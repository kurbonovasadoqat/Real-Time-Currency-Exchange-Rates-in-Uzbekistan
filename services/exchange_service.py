# currency_bot/services/exchange_service.py

import httpx
from services.texts import texts
from decimal import Decimal

OPEN_ER_API = "https://open.er-api.com/v6/latest/USD"
CBU_ARCHIVE_URL="https://cbu.uz/oz/arkhiv-kursov-valyut/json/"


async def get_international_rate(lang: str = "en") -> str:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(OPEN_ER_API)
            data = response.json()

        rates = data.get("rates", {})
        uzs = Decimal(str(rates.get("UZS", 0)))
        eur = Decimal(str(rates.get("EUR", 0)))
        rub = Decimal(str(rates.get("RUB", 0)))

        return texts["international_multi"][lang].format(
            uzs=f"{uzs:,.2f}",
            eur=f"{eur:.2f}",
            rub=f"{rub:.2f}"
        )
    except Exception:
        return texts["international_error"].get(lang, texts["international_error"]["en"])
    
async def get_cbu_rate(lang: str = "en") -> str:
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(CBU_ARCHIVE_URL)
            data = response.json()

        rates = {
            item["Ccy"]: Decimal(item.get("Rate", "0"))
            for item in data
        }

        usd = rates.get("USD", Decimal("0"))
        eur = rates.get("EUR", Decimal("0"))
        rub = rates.get("RUB", Decimal("0"))

        return texts["cbu_success"][lang].format(
            usd=f"{usd:,.2f}",
            eur=f"{eur:,.2f}",
            rub=f"{rub:,.2f}"
        )

    except Exception:
        return texts["cbu_error"].get(lang, texts["cbu_error"]["en"])