from app.domain.models import Transaction


class TransactionRepository:
    def __init__(self):
        self._transactions = []

    def save(self, transaction: Transaction) -> None:
        self._transactions.append(transaction)

    def get_all(self) -> list[Transaction]:
        return self._transactions