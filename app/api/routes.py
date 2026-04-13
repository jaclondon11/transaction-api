from fastapi import APIRouter, Depends

from app.api.dependencies import get_transaction_service
from app.domain.models import Transaction
from app.services.transaction_service import TransactionService

router = APIRouter()

@router.post("/transactions")
def create_transaction(
    amount: float,
    customer_type: str,
    channel: str,
    service: TransactionService = Depends(get_transaction_service),
):
    transaction = Transaction.create(amount, customer_type, channel)
    return service.create_transaction(transaction)

@router.get("/transactions")
def get_transactions(
    service: TransactionService = Depends(get_transaction_service),
):
    return service.get_transactions()