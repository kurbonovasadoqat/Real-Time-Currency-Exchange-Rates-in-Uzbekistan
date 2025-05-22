# currency_bot/services/converter.py

def convert_currency(amount: float, from_cur: str, to_cur: str, rates: dict) -> float:
    from_cur = from_cur.upper()
    to_cur = to_cur.upper()

    if from_cur not in rates or to_cur not in rates:
        raise ValueError(f"Kurs topilmadi: {from_cur} → {to_cur}")

    if from_cur == "UZS":
        return amount / rates[to_cur]
    elif to_cur == "UZS":
        return amount * rates[from_cur]
    else:
        return amount * (rates[from_cur] / rates[to_cur])
