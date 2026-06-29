from decimal import Decimal
import requests
from decouple import config

EXCHANGE_RATE_API_KEY = config("EXCHANGE_RATE_API_KEY")


def convert_currency(amount: Decimal, from_currency: str, to_currency: str) -> Decimal:
    if from_currency == to_currency:
        return amount
    
    try:
        response = requests.get(
            f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{from_currency}/{to_currency}"
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise requests.exceptions.HTTPError(f"Failed to convert {from_currency} to {to_currency}: {response.status_code}")
    rate = Decimal(str(response.json()["conversion_rate"]))
    return rate * amount