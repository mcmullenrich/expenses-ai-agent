from abc import ABC


class ExpenseRepository(ABC):
    pass


class InMemoryExpenseRepository(ExpenseRepository):
    pass