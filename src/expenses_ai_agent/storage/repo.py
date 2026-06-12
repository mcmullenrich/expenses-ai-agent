from abc import ABC, abstractmethod
from expenses_ai_agent.storage.models import Expense
from expenses_ai_agent.storage.exceptions import ExpenseNotFoundError


class ExpenseRepository(ABC):
    @abstractmethod
    def add(self, expense) -> None:
        pass

    @abstractmethod
    def get(self, id: int) -> Expense | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Expense]:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def search_by_category(self, expense_category) -> list[Expense]:
        pass


class InMemoryExpenseRepository(ExpenseRepository):
    def __init__(self):
        self.expenses = {}
        self.id = 0

    def add(self, expense):
        self.id += 1
        expense.id = self.id
        self.expenses[self.id] = expense

    def delete(self, id):
        if id in self.expenses.keys():
            del self.expenses[id]
        else:
            raise ExpenseNotFoundError(id)

    def get(self, id):
        return self.expenses.get(id)

    def get_all(self):
        return list(self.expenses.values())

    def search_by_category(self, expense_category):
        return [e for e in self.expenses.values() if e.category == expense_category]
