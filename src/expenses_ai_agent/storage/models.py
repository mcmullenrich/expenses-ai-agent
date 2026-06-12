from enum import StrEnum
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from decimal import Decimal

def _utc_now() -> datetime:
    return datetime.now(timezone.utc)

class Currency(StrEnum):
    EUR = "EUR"
    USD = "USD"
    GBP = "GBP"
    JPY = "JPY"
    CHF = "CHF"
    CAD = "CAD"
    AUD = "AUD"
    CNY = "CNY"
    INR = "INR"
    MXN = "MXN"

class ExpenseCategory(StrEnum):
    FOOD = "Food"
    TRANSPORT = "Transport"
    ENTERTAINMENT = "Entertainment"
    SHOPPING = "Shopping"
    HEALTH = "Health"
    BILLS = "Bills"
    EDUCATION = "Education"
    TRAVEL = "Travel"
    SERVICES = "Services"
    GIFTS = "Gifts"
    INVESTMENTS = "Investments"
    OTHER = "Other"

class Expense(SQLModel, table=True):
     id: int | None = Field(default=None, primary_key=True)
     amount: Decimal
     currency: Currency = Currency.EUR
     description: str | None = Field(default=None)
     date: datetime = Field(default_factory=_utc_now)
     category: ExpenseCategory | None = Field(default=None)
     telegram_user_id: int | None = Field(default=None)

     def __str__(self):
        return f"{self.amount} {self.currency}"
     
     @classmethod
     def create(cls, amount, currency, description, category):
         return Expense(amount=amount, currency=currency, description=description, category=category)