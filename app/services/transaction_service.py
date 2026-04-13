from collections.abc import Sequence

from app.domain.models import Transaction, TransactionStatus
from app.domain.ports import TransactionRepository, TransactionRule

class TransactionService:
    def __init__(
        self,
        repository: TransactionRepository,
        rules: Sequence[TransactionRule],
    ):
        self.repository = repository
        self.rules = tuple(rules)

    def create_transaction(self, transaction: Transaction) -> Transaction:
        if any(not rule.evaluate(transaction) for rule in self.rules):
            transaction.status = TransactionStatus.REJECTED

        self.repository.save(transaction)
        return transaction

    def get_transactions(self) -> list[Transaction]:
        return self.repository.get_all()