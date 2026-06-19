from decimal import Decimal
from enum import StrEnum
from typing import Protocol, Sequence

from expenses_ai_agent.llms.output import ExpenseCategorizationResponse

MESSAGES = list[dict[str, str]]
COST = dict[str, list[Decimal]]

class LLMProvider(StrEnum):
    OPENAI = "OPENAI"
    GROQ = "GROQ"

class Assistant(Protocol):
    
    def completion(self, messages: MESSAGES) -> ExpenseCategorizationResponse:
        ...

    def calculate_cost(self, prompt_tokens: int, completion_tokens: int) -> Decimal:
        ...

    def get_available_models(self) -> Sequence[str]:
        ...