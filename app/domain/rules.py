from app.domain.models import Transaction
from app.domain.ports import TransactionRule


class AmountLimitRule(TransactionRule):
    def __init__(self, limit: float):
        self.limit = limit

    def evaluate(self, transaction: Transaction) -> bool:
        return transaction.amount <= self.limit