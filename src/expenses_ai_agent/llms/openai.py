from decouple import config
from openai import OpenAI
from decimal import Decimal
from typing import Any, cast
from expenses_ai_agent.llms.base import MESSAGES
from expenses_ai_agent.llms.output import ExpenseCategorizationResponse
from expenses_ai_agent.storage.exceptions import EmptyResponseError

MODEL_MAP = {
    "gpt-4o-mini": (Decimal("0.00000015"), Decimal("0.0000006"))
}

class OpenAIAssistant:
    def __init__(self, model: str = "gpt-4o-mini", api_key: str | None = None):
        self.api_key = api_key or config("OPENAI_API_KEY", default="")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model

    def completion(self, messages: MESSAGES) -> ExpenseCategorizationResponse:
        response = self.client.beta.chat.completions.parse(
            messages=cast(Any, messages),
            model=self.model,
            response_format=ExpenseCategorizationResponse,
        )
        result = response.choices[0].message.parsed
        if result is None:
            raise EmptyResponseError("Failed to parse response from OpenAI")

        if response.usage is not None:
            result.cost = self.calculate_cost(
                response.usage.prompt_tokens,
                response.usage.completion_tokens,
            )

        return result

    def calculate_cost(self, prompt_tokens: int, completion_tokens: int) -> Decimal:
        try:
            cost = (prompt_tokens * MODEL_MAP[self.model][0]) + (completion_tokens * MODEL_MAP[self.model][1])
        except KeyError:
            raise KeyError(f"Model '{self.model}' is not in MODEL_MAP")
        return cost

    def get_available_models(self) -> list[str]:
        return [x.id for x in self.client.models.list()]
