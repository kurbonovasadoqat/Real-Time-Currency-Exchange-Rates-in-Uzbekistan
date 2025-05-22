# currency_bot/providers/fca_provider.py

import httpx
import os
from interfaces.rate_provider_interface import RateProviderInterface

class FreeCurrencyAPIProvider(RateProviderInterface):
    BASE_URL = "https://api.freecurrencyapi.com/v1/latest"
    API_KEY = os.getenv("FREECURRENCY_API_KEY")

    async def get_rate(self, from_currency: str, to_currency: str) -> float:
        url = f"{self.BASE_URL}?apikey={self.API_KEY}&base_currency={from_currency.upper()}"
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
            data = resp.json()
        return float(data["data"][to_currency.upper()])
