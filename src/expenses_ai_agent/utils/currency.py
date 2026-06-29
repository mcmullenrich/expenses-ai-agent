from decimal import Decimal
import requests
from decouple import config

def convert_currency(amount: Decimal, from_currency: str, to_currency: str, exchange_rate_key=None) -> Decimal:
    exchange_rate_key = exchange_rate_key or config("EXCHANGE_RATE_API_KEY", default="")
    url = f"https://v6.exchangerate-api.com/v6/{exchange_rate_key}/pair/{from_currency}/{to_currency}"
    if from_currency == to_currency:
        return amount
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except (requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout) as e:
        raise RuntimeError(f"Currency conversion failed: {e}") from e
    data = response.json()
    if data.get("result") != "success":
        raise RuntimeError(f"Exchange rate API error: {data.get('error', 'unknown')}")
    rate = Decimal(str(data["conversion_rate"]))
    return rate * amount