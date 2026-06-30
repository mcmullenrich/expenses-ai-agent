class ExpenseNotFoundError(Exception):
    def __init__(self, id):
        self.id = id
        super().__init__(id)

class EmptyResponseError(Exception):
    pass