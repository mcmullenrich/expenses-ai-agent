from abc import ABC, abstractmethod
from expenses_ai_agent.storage.models import Expense, ExpenseCategory
from expenses_ai_agent.storage.exceptions import ExpenseNotFoundError


class ExpenseRepository(ABC):
    @abstractmethod
    def add(self, expense: Expense) -> None:
        pass

    @abstractmethod
    def get(self, id_: int) -> Expense | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Expense]:
        pass

    @abstractmethod
    def delete(self, id_: int) -> None:
        pass

    @abstractmethod
    def search_by_category(self, expense_category: ExpenseCategory) -> list[Expense]:
        pass


class InMemoryExpenseRepository(ExpenseRepository):
    def __init__(self) -> None:
        self.expenses = {}
        self.id = 0

    def add(self, expense: Expense) -> None:
        self.id += 1
        expense.id = self.id
        self.expenses[self.id] = expense

    def delete(self, id_: int) -> None:
        try:
            del self.expenses[id_]
        except KeyError:
            raise ExpenseNotFoundError(id_)

    def get(self, id_: int) -> Expense | None:
        return self.expenses.get(id_)

    def get_all(self) -> list[Expense]:
        return list(self.expenses.values())

    def search_by_category(self, expense_category: ExpenseCategory) -> list[Expense]:
        return [e for e in self.expenses.values() if e.category == expense_category]
