# currency_bot/services/crypto_service.py

import aiohttp
import json

CRYPTO_SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT", "DOGEUSDT"]

async def get_crypto_prices():
    url = "https://api.binance.com/api/v3/ticker/price"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

        btc_price = None
        eth_price = None

        for item in data:
            if item["symbol"] == "BTCUSDT":
                btc_price = float(item["price"])
            elif item["symbol"] == "ETHUSDT":
                eth_price = float(item["price"])

        if btc_price is None or eth_price is None:
            raise ValueError("Kripto narxlar topilmadi")

        return btc_price, eth_price

    except Exception as e:
        print("❌ Kripto narxlar olishda xatolik:", e)
        return None, None