# currency_bot/providers/currencylayer_provider.py

import httpx
import os
from interfaces.rate_provider_interface import RateProviderInterface

class CurrencyLayerProvider(RateProviderInterface):
    BASE_URL = "http://api.currencylayer.com/live"
    API_KEY = os.getenv("CURRENCYLAYER_API_KEY")

    async def get_rate(self, from_currency: str, to_currency: str) -> float:
        url = f"{self.BASE_URL}?access_key={self.API_KEY}&source={from_currency.upper()}&currencies={to_currency.upper()}"
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
            data = resp.json()
        return float(data["quotes"][f"{from_currency.upper()}{to_currency.upper()}"])
