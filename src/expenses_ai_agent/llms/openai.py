from decouple import config
from openai import OpenAI
from decimal import Decimal
from typing import Any, cast
from expenses_ai_agent.llms.base import MESSAGES
from expenses_ai_agent.llms.output import ExpenseCategorizationResponse

OPENAI_API_KEY = config("OPENAI_API_KEY")


class OpenAIAssistant:
    def __init__(self, model: str = "gpt-4o-mini", api_key: str | None = None):
        if api_key is None:
            api_key = OPENAI_API_KEY

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def completion(self, messages: MESSAGES) -> ExpenseCategorizationResponse:
        response = self.client.beta.chat.completions.parse(
            messages=cast(Any, messages),
            model=self.model,
            response_format=ExpenseCategorizationResponse,
        )
        result = response.choices[0].message.parsed
        if result is None:
            raise ValueError("Failed to parse response from OpenAI")

        if response.usage:
            result.cost = self.calculate_cost(
                response.usage.prompt_tokens,
                response.usage.completion_tokens,
            )

        return result

    def calculate_cost(self, prompt_tokens, completion_tokens) -> Decimal:
        cost = (prompt_tokens * Decimal("0.00000015")) + (
            completion_tokens * Decimal("0.0000006")
        )
        return cost

    def get_available_models(self) -> list[str]:
        return [x.id for x in self.client.models.list()]
