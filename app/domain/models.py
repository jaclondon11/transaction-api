from pydantic import BaseModel
from enum import Enum
from uuid import uuid4

class TransactionStatus(str, Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class Transaction(BaseModel):
    id: str
    amount: float
    customer_type: str
    channel: str
    status: TransactionStatus

    @staticmethod
    def create(amount: float, customer_type: str, channel: str):
        return Transaction(
            id=str(uuid4()),
            amount=amount,
            customer_type=customer_type,
            channel=channel,
            status=TransactionStatus.APPROVED
        )