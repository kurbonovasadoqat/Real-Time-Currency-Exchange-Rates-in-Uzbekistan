# currency_bot/providers/fixer_provider.py

import httpx
import os
from interfaces.rate_provider_interface import RateProviderInterface

class FixerAPIProvider(RateProviderInterface):
    BASE_URL = "http://data.fixer.io/api/latest"
    API_KEY = os.getenv("FIXER_API_KEY")

    async def get_rate(self, from_currency: str, to_currency: str) -> float:
        url = f"{self.BASE_URL}?access_key={self.API_KEY}&base={from_currency.upper()}&symbols={to_currency.upper()}"
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
            data = resp.json()
        return float(data["rates"][to_currency.upper()])
