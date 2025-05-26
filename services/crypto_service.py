# ✅ CACHED CRYPTO SERVICE
# currency_bot/services/crypto_service.py

from aiohttp import ClientSession
from aiocache import cached, Cache

@cached(ttl=300, cache=Cache.MEMORY)
async def get_crypto_prices():
    url = "https://api.binance.com/api/v3/ticker/price?symbols=[\"BTCUSDT\",\"ETHUSDT\"]"
    try:
        async with ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

        btc = next(item["price"] for item in data if item["symbol"] == "BTCUSDT")
        eth = next(item["price"] for item in data if item["symbol"] == "ETHUSDT")

        return float(btc), float(eth)

    except Exception:
        return None, None