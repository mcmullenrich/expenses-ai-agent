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

## Up Next — Week 2
- Create a new branch: `week2`
- Check course materials for Week 2 tasks

## Lessons Covered
- 03: Environment Setup
- 04: Repository Pattern
- 05: SQLModel Entities
- 06: Python Enums with StrEnum
- 07: Week 1 Implementation ✅