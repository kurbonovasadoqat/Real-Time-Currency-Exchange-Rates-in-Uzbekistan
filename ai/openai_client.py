# currency_bot/ai/openai_client.py

import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("❌ OPENAI_API_KEY topilmadi. .env faylga qo‘shing.")

client = AsyncOpenAI(api_key=api_key)

async def chat_completion(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that returns only JSON."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ OpenAI xatoligi:", e)
        raise RuntimeError("OpenAI bilan bog‘lanishda xatolik yuz berdi.")
