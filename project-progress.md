# Agentic AI Course — Progress

## Environment
- OS: Windows 11, PowerShell + Git Bash (via VS Code terminal)
- Python: 3.14.6
- Package manager: uv 0.11.21
- Editor: VS Code with Python, Pylance, and Ruff extensions configured

## Project
- Repo: https://github.com/mcmullenrich/expenses-ai-agent
- Working directory: `C:\Users\rmcmullen\expenses-ai-agent`

## Windows-Specific Notes
- `mkdir -p` does not work in PowerShell — use `mkdir folder1, folder2` or Git Bash
- `touch` does not work in PowerShell — use `New-Item file -ItemType File` or Git Bash
- `curl` in PowerShell is an alias for `Invoke-WebRequest` — use `Invoke-WebRequest -Uri "..." -OutFile "..."` or Git Bash
- Git Bash (available in VS Code terminal dropdown) supports Linux commands exactly as written in the course instructions
- Recommended: use Git Bash terminal in VS Code to follow course instructions without translation
- Always run `pwd` before `git clone` or `uv init` to avoid nested repo issues

## Week 1 — COMPLETE ✅
- Branch: `week1` — PR submitted, reviewed, and feedback addressed
- All 24 tests passing

### Steps Completed
- Step 0: Package structure
- Step 1: `Currency` StrEnum (10 ISO 4217 codes)
- Step 2: `ExpenseCategory` StrEnum (12 categories, title case values)
- Step 3: `ExpenseNotFoundError` custom exception
- Step 4: `Expense` SQLModel entity
- Step 5: `ExpenseRepository` abstract base class
- Step 6: `InMemoryExpenseRepository` backed by a dictionary

### PR Feedback Addressed
- Added type hints to `Expense.create()` in `models.py`
- Changed `Expense(...)` to `cls(...)` in `Expense.create()`
- Added type hints throughout `ExpenseRepository` and `InMemoryExpenseRepository` in `repo.py`
- Renamed `id` parameter to `id_` to avoid shadowing Python built-in
- Converted `delete()` to "ask for forgiveness" style (`try/except KeyError`)

### Key Learnings
- `@classmethod` receives the class as `cls`, not an instance — use `cls(...)` not `ClassName(...)`
- Type hints don't enforce at runtime but enable static analysis with `ty`
- "Ask for forgiveness" (`try/except`) is preferred over "look before you leap" (`if/else`) in Python
- Avoid using `id` as a parameter name — it shadows the built-in `id()` function
- Forward references in type hints: use `-> "Expense"` when inside the class being referenced

## Week 2 — IN PROGRESS 🔄
- Branch: `week2` — PR open, second round of feedback addressed, awaiting approval
- All 60 tests passing, `uv run ty check .` clean

### Steps Completed
- Step 1: `ExpenseCategorizationResponse` Pydantic model (`llms/output.py`)
- Step 2: Type aliases (`MESSAGES`, `COST`) and `Assistant` Protocol (`llms/base.py`)
- Step 3: `convert_currency` utility with ExchangeRate API (`utils/currency.py`)
- Step 4: `format_datetime` utility with timezone support (`utils/date_formatter.py`)
- Step 5: Tool schemas for OpenAI function calling (`tools/tools.py`)
- Step 6: `OpenAIAssistant` implementation (`llms/openai.py`)

### PR Feedback Addressed (Round 1)
- Moved `OPENAI_API_KEY` config read from module level into `__init__` (lazy config pattern)
- Replaced hardcoded prices in `calculate_cost` with `MODEL_MAP` dict and `ModelConstants` Pydantic class
- Added `try/except KeyError` to `calculate_cost` for unsupported models
- Added type hints to `calculate_cost` parameters
- Added HTTP error handling to `convert_currency` with `raise_for_status()`
- Removed redundant `else` after early `return` in `convert_currency`
- Added `try/except ValueError` to `format_datetime` for invalid datetime strings
- Changed `if response.usage` to `if response.usage is not None`
- Added `EmptyResponseError` custom exception to `storage/exceptions.py`
- Changed `category: str` to `category: ExpenseCategory` in `ExpenseCategorizationResponse`
- Added `Field(ge=0.0, le=1.0)` to `confidence` in `ExpenseCategorizationResponse`
- Added `dict[str, Any]` type hints to tool schema constants in `tools/tools.py`
- Updated test file to use `ExpenseCategory` enum values instead of plain strings

### PR Feedback Addressed (Round 2)
- Moved `EXCHANGE_RATE_API_KEY` from module level into `convert_currency` as a parameter (lazy config pattern)
- Added `timeout=10` to `requests.get()` in `convert_currency`
- Broadened exception handling in `convert_currency` to catch `ConnectionError` and `Timeout` in addition to `HTTPError`
- Added check for `data.get("result") != "success"` to catch API errors that return 200 with error body
- Added `try/except ZoneInfoNotFoundError` to `format_datetime` for invalid timezone strings
- Fixed tool schema `amount` field from `"type": "string"` to `"type": "number"`
- Added `if not self.api_key: raise ValueError` to fail fast on missing API key
- Stored `GPT_4O_MINI` object directly as `MODEL_MAP` value instead of unpacking into a tuple
- Added new tests: `confidence` out of range raises `ValidationError`, `EmptyResponseError` on `None` response, `KeyError` on unsupported model, `result.cost` value assertion

### Key Learnings
- Module-level `config()` reads crash imports if env vars are missing — always read lazily inside `__init__` or as a function parameter
- `if x is not None` is more explicit than `if x` — use it when checking for `None` specifically
- Early returns eliminate the need for `else` — drop it for cleaner, more idiomatic Python
- `response.raise_for_status()` automatically raises `HTTPError` on bad responses
- Always add `timeout=` to `requests.get()` — without it the request can hang indefinitely
- APIs can return 200 with an error body — always check the response payload, not just the status code
- `dict[str, Any]` is the right type hint for deeply nested dictionaries
- Custom exceptions are more descriptive than generic ones (`EmptyResponseError` vs `ValueError`)
- Pydantic `Field(ge=0.0, le=1.0)` enforces value ranges at runtime
- Variable type annotations use `:` not `->` (e.g. `CONSTANT: dict[str, Any] = {...}`)
- Pydantic `BaseModel` can be used for configuration/constants, not just API response models
- Storing a Pydantic object as a dict value is cleaner than unpacking its fields into a tuple
- `pytest.raises(ExceptionType)` is used in tests to assert that a specific exception is raised
- Fail fast on missing config — an empty string API key produces a confusing late error; raise early instead

## Lessons Covered
- 03: Environment Setup
- 04: Repository Pattern
- 05: SQLModel Entities
- 06: Python Enums with StrEnum
- 07: Week 1 Implementation ✅
- 08–13: Week 2 Implementation (Protocols, Pydantic, type aliases, external APIs, tool schemas, OpenAI assistant)