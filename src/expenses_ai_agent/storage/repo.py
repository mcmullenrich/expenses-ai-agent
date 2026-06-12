from abc import ABC, abstractmethod


class ExpenseRepository(ABC):
    @abstractmethod
    def add_expense(self):
        pass


class InMemoryExpenseRepository(ExpenseRepository):
    pass