# currency_bot/services/ai_parser_service.py

import json
from ai.openai_client import chat_completion

async def extract_conversion_info(user_text: str, lang: str = "en") -> dict:
    prompt = f"""
You are a smart assistant for currency conversion.

Extract 3 values from this user input:
- "amount": number
- "from_currency": ISO code
- "to_currency": ISO code

User language: {lang}
User input: "{user_text}"

Return only JSON format:
{{ "amount": 100, "from_currency": "USD", "to_currency": "UZS" }}
"""

    try:
        response = await chat_completion(prompt)
        return json.loads(response)
    except json.JSONDecodeError:
        return {}
