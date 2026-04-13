import pytest
from pydantic import ValidationError

from app.domain.models import (
    CreateTransactionRequest,
    CustomerType,
    Transaction,
    TransactionChannel,
    TransactionStatus,
)
from app.domain.rules import AmountLimitRule
from app.infrastructure.repository import TransactionRepository
from app.services.transaction_service import TransactionService


def build_service(limit: float = 1000) -> TransactionService:
    repository = TransactionRepository()
    rules = (AmountLimitRule(limit=limit),)
    return TransactionService(repository=repository, rules=rules)


def test_create_transaction_approves_when_within_limit() -> None:
    service = build_service(limit=1000)
    transaction = Transaction.create(
        amount=250,
        customer_type=CustomerType.INDIVIDUAL,
        channel=TransactionChannel.WEB,
    )

    result = service.create_transaction(transaction)

    assert result.status == TransactionStatus.APPROVED


def test_create_transaction_rejects_when_above_limit() -> None:
    service = build_service(limit=1000)
    transaction = Transaction.create(
        amount=1500,
        customer_type=CustomerType.BUSINESS,
        channel=TransactionChannel.POS,
    )

    result = service.create_transaction(transaction)

    assert result.status == TransactionStatus.REJECTED


def test_get_transactions_returns_saved_transactions() -> None:
    service = build_service(limit=1000)
    transaction = Transaction.create(
        amount=500,
        customer_type=CustomerType.INDIVIDUAL,
        channel=TransactionChannel.MOBILE,
    )
    service.create_transaction(transaction)

    all_transactions = service.get_transactions()

    assert len(all_transactions) == 1
    assert all_transactions[0].id == transaction.id


def test_create_transaction_request_requires_positive_amount() -> None:
    with pytest.raises(ValidationError):
        CreateTransactionRequest(
            amount=0,
            customer_type=CustomerType.INDIVIDUAL,
            channel=TransactionChannel.WEB,
        )
