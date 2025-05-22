import pytest
import asyncio
from ai.ai_parser import extract_conversion_info

# Test holatlar
test_cases = [
    # Format: (user_input, expected_from, expected_to, expected_amount)

    ("100 usd to uzs", "USD", "UZS", 100),
    ("btc to uzs", "BTC", "UZS", 1),
    ("so'mdan dollarga", "UZS", "USD", 1),
    ("yevro dollar", "EUR", "USD", 1),
    ("usdt token to rub", "USDT", "RUB", 1),
    ("250 rublni yevroga aylantir", "RUB", "EUR", 250),
    ("btc", None, None, None),  # noto‘liq
    ("", None, None, None),     # bo‘sh
]

@pytest.mark.asyncio
@pytest.mark.parametrize("user_input, expected_from, expected_to, expected_amount", test_cases)
async def test_extract_conversion_info(user_input, expected_from, expected_to, expected_amount):
    result = await extract_conversion_info(user_input, lang="en")

    if expected_from is None:
        assert result == {} or result.get("from_currency") is None
    else:
        assert result["from_currency"] == expected_from
        assert result["to_currency"] == expected_to
        assert round(result["amount"], 2) == expected_amount
