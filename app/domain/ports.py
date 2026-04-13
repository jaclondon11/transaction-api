from typing import Protocol, Sequence

from app.domain.models import Transaction


class TransactionRepository(Protocol):
    def save(self, transaction: Transaction) -> None:
        ...

    def get_all(self) -> Sequence[Transaction]:
        ...


class TransactionRule(Protocol):
    def evaluate(self, transaction: Transaction) -> bool:
        ...