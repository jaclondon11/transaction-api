import pytest
from fastapi.testclient import TestClient

from app.api.dependencies import get_transaction_service
from app.domain.rules import AmountLimitRule
from app.infrastructure.repository import TransactionRepository
from app.main import app
from app.services.transaction_service import TransactionService


@pytest.fixture
def client() -> TestClient:
    repository = TransactionRepository()
    rules = (AmountLimitRule(limit=1000),)
    service = TransactionService(repository=repository, rules=rules)

    app.dependency_overrides[get_transaction_service] = lambda: service
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


def test_create_transaction_returns_expected_response_shape(client: TestClient) -> None:
    response = client.post(
        "/transactions",
        json={
            "amount": 250.0,
            "customer_type": "INDIVIDUAL",
            "channel": "WEB",
        },
    )

    assert response.status_code == 200

    body = response.json()
    assert set(body.keys()) == {"id", "amount", "customer_type", "channel", "status"}
    assert body["amount"] == 250.0
    assert body["customer_type"] == "INDIVIDUAL"
    assert body["channel"] == "WEB"
    assert body["status"] == "APPROVED"


def test_create_transaction_rejects_amount_above_limit(client: TestClient) -> None:
    response = client.post(
        "/transactions",
        json={
            "amount": 1500.0,
            "customer_type": "BUSINESS",
            "channel": "POS",
        },
    )

    assert response.status_code == 200
    assert response.json()["status"] == "REJECTED"


def test_create_transaction_requires_positive_amount(client: TestClient) -> None:
    response = client.post(
        "/transactions",
        json={
            "amount": 0,
            "customer_type": "INDIVIDUAL",
            "channel": "WEB",
        },
    )

    assert response.status_code == 422


def test_create_transaction_rejects_invalid_channel(client: TestClient) -> None:
    response = client.post(
        "/transactions",
        json={
            "amount": 100.0,
            "customer_type": "INDIVIDUAL",
            "channel": "EMAIL",
        },
    )

    assert response.status_code == 422
