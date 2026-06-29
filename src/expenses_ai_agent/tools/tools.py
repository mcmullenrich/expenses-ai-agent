from typing import Any

CURRENCY_CONVERSION_TOOL: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "currency_conversion_tool",
        "description": "Convert from one currency to another currency.",
        "parameters": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "string",
                    "description": "The amount of from_currency to be converted to to_currency.",
                },
                "from_currency": {
                    "type": "string",
                    "description": "The currency we are converting from.",
                },
                "to_currency": {
                    "type": "string",
                    "description": "The currency we are converting to.",
                },
            },
            "required": ["amount", "from_currency", "to_currency"],
        },
    },
}

DATETIME_FORMATTER_TOOL: dict[str, Any] = {
    "type": "function",
    "function": {
        "name": "datetime_formatter_tool",
        "description": "Format a datetime.",
        "parameters": {
            "type": "object",
            "properties": {
                "datetime_str": {
                    "type": "string",
                    "description": "A datetime that you want to format.",
                },
                "timezone_str": {
                    "type": "string",
                    "description": "A timzone associated with the datetime.",
                },
            },
            "required": ["datetime_str"],
        },
    },
}
