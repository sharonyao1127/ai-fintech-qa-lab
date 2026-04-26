from fastapi.testclient import TestClient
from mock_payment_service.main import app, users, payments


client = TestClient(app)


def setup_function():
    users["user_001"] = {
        "eligibility_status": "approved",
        "payment_feature_status": "disabled",
        "balance": 1000,
    }
    payments.clear()


def test_duplicate_payment_request_should_not_deduct_balance_twice():
    client.post("/payment-feature/enable", params={"user_id": "user_001"})

    payload = {
        "request_id": "req_001",
        "user_id": "user_001",
        "amount": 100,
        "transaction_id": "tx_001",
    }

    first = client.post("/payments/process", json=payload)
    second = client.post("/payments/process", json=payload)
    balance = client.get("/balance/user_001")

    assert first.status_code == 200
    assert first.json()["status"] == "processed"

    assert second.status_code == 200
    assert second.json()["status"] == "duplicate_ignored"

    assert balance.json()["balance"] == 900
    assert len(payments) == 1
