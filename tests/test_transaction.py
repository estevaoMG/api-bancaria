from src.controllers import transaction as transaction_controller

# =========================
# Service
# =========================
service = transaction_controller.service


# =========================
# Constantes
# =========================
FIXED_TIMESTAMP = "2026-01-01T00:00:00+00:00"


# =========================
# Builders
# =========================


def transaction_payload(account_id=1, amount=100, type_="deposit"):
    return {
        "account_id": account_id,
        "amount": amount,
        "type": type_,
    }


def transaction_expected():
    return {
        "id": 1,
        "account_id": 1,
        "amount": 100,
        "type": "deposit",
        "timestamp": FIXED_TIMESTAMP,
    }


# =========================
# Helpers de assert
# =========================


def assert_transaction(data: dict):
    assert data["id"] == 1
    assert data["account_id"] == 1
    assert data["amount"] == 100
    assert data["type"] == "deposit"

    # timestamp NÃO é comparado como string fixa (evita Z vs +00:00)
    assert "timestamp" in data
    assert isinstance(data["timestamp"], str)


# =========================
# Tests
# =========================


def test_create_transaction(client, monkeypatch):

    async def fake_create(transaction):
        return {
            "id": 1,
            "account_id": transaction.account_id,
            "amount": transaction.amount,
            "type": transaction.type,
            "timestamp": FIXED_TIMESTAMP,
        }

    monkeypatch.setattr(service, "create", fake_create)

    response = client.post(
        "/transactions/",
        json=transaction_payload(),
    )

    assert response.status_code in (200, 201)

    assert_transaction(response.json())
