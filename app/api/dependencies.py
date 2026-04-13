from functools import lru_cache

from fastapi import Depends

from app.domain.rules import AmountLimitRule
from app.infrastructure.repository import TransactionRepository
from app.services.transaction_service import TransactionService


@lru_cache
def get_repository() -> TransactionRepository:
    return TransactionRepository()


def get_transaction_rules() -> tuple[AmountLimitRule, ...]:
    return (AmountLimitRule(limit=1000),)


def get_transaction_service(
    repo: TransactionRepository = Depends(get_repository),
    rules: tuple[AmountLimitRule, ...] = Depends(get_transaction_rules),
) -> TransactionService:
    return TransactionService(repository=repo, rules=rules)