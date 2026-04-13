from pydantic import BaseModel, Field
from enum import Enum
from uuid import uuid4


class TransactionStatus(str, Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class CustomerType(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    BUSINESS = "BUSINESS"


class TransactionChannel(str, Enum):
    WEB = "WEB"
    MOBILE = "MOBILE"
    POS = "POS"


class CreateTransactionRequest(BaseModel):
    amount: float = Field(gt=0)
    customer_type: CustomerType
    channel: TransactionChannel


class Transaction(BaseModel):
    id: str
    amount: float
    customer_type: CustomerType
    channel: TransactionChannel
    status: TransactionStatus

    @staticmethod
    def create(
        amount: float,
        customer_type: CustomerType,
        channel: TransactionChannel,
    ):
        return Transaction(
            id=str(uuid4()),
            amount=amount,
            customer_type=customer_type,
            channel=channel,
            status=TransactionStatus.APPROVED
        )