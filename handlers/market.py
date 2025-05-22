# currency_bot/handlers/market.py

from aiogram import Router, F
from aiogram.types import Message
import logging

from services.exchange_service import get_cbu_rate, get_international_rate
from services.blackmarket_service import get_blackmarket_rates
from services.crypto_service import get_crypto_prices
from services.user_service import get_user_language
from services.texts import texts
from keyboards.menu_buttons import main_menu_keyboard

router = Router()

# Tugma matnlari (3 tilda)
CBU = ["🏦 Markaziy Bank", "🏦 Центральный Банк", "🏦 Central Bank"]
BLACK = ["⚫ Qora Bozor", "⚫ Черный рынок", "⚫ Black Market"]
INTERNATIONAL = ["🌍 Xalqaro Kurslar", "🌍 Международные курсы", "🌍 International Rates"]
CRYPTO = ["💱 Kripto valyutalar", "💱 Криптовалюты", "💱 Crypto Prices"]


# 🏦 Markaziy Bank kursi
@router.message(F.text.in_(CBU))
async def show_cbu_rate(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)

    try:
        text = await get_cbu_rate(lang)
    except Exception:
        logging.exception("❌ CBU kursi olishda xatolik")
        text = texts["cbu_error"].get(lang, texts["cbu_error"]["en"])

    await message.answer(text, reply_markup=main_menu_keyboard(lang))


# ⚫ Qora bozor kursi
@router.message(F.text.in_(BLACK))
async def show_black_rate(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)

    try:
        text = await get_blackmarket_rates(lang)
    except Exception:
        logging.exception("❌ Qora bozor kursi olishda xatolik")
        text = texts["black_error"].get(lang, texts["black_error"]["en"])

    await message.answer(text, reply_markup=main_menu_keyboard(lang))


# 🌍 Xalqaro kurslar
@router.message(F.text.in_(INTERNATIONAL))
async def show_international_rate(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)

    try:
        text = await get_international_rate(lang)
    except Exception:
        logging.exception("❌ Xalqaro kurslar olishda xatolik")
        text = texts["international_error"].get(lang, texts["international_error"]["en"])

    await message.answer(text, reply_markup=main_menu_keyboard(lang))


# 💱 Kripto narxlar (BTC / ETH)
@router.message(F.text.in_(CRYPTO))
async def show_crypto_prices(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)

    try:
        btc, eth = await get_crypto_prices()
        if btc is None or eth is None:
            raise ValueError("No crypto data")

        template = texts["crypto_success"].get(lang, texts["crypto_success"]["en"])
        text = template.format(btc=f"{btc:,.2f}", eth=f"{eth:,.2f}")

    except Exception:
        logging.exception("❌ Crypto narxlar olishda xatolik")
        text = texts["crypto_error"].get(lang, texts["crypto_error"]["en"])

    await message.answer(text, reply_markup=main_menu_keyboard(lang))
