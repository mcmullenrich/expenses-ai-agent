from pydantic import BaseModel, Field
from expenses_ai_agent.storage.models import Currency, ExpenseCategory
from decimal import Decimal
from datetime import timezone, datetime

class ExpenseCategorizationResponse(BaseModel):
    category: ExpenseCategory
    total_amount: Decimal = Field(
        description="Numeric amount extracted from the expense description"
    )
    currency: Currency = Field(
        description="Currency code from the description, default EUR"
    )
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score 0.0-1.0")
    cost: Decimal = Field(
        default=Decimal("0"),
        description="Leave as 0 — set programmatically after the API call",
    )
    comments: str | None = Field(default=None)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
