from datetime import datetime, timezone

from src.controllers import account as account_controller

# =========================
# Constantes
# =========================

FIXED_DATETIME = "2026-01-01T00:00:00+00:00"

account_service = account_controller.account_service
tx_service = account_controller.tx_service


# =========================
# Helpers
# =========================


def account_payload(user_id=1, balance=1000):
    return {"user_id": user_id, "balance": balance}


def build_account(account_id=1, user_id=1, balance=1000):
    return {
        "id": account_id,
        "user_id": user_id,
        "balance": balance,
        "created_at": FIXED_DATETIME,
    }


def build_transaction(account_id=1):
    return [
        {
            "id": 1,
            "account_id": account_id,
            "amount": 100,
            "type": "deposit",
            "timestamp": FIXED_DATETIME,
        }
    ]


# =========================
# Normalização de datetime (FIX do erro Z vs +00:00)
# =========================


def normalize_datetime(value: str):
    if isinstance(value, str) and value.endswith("Z"):
        return value.replace("Z", "+00:00")
    return value


def assert_json(response, expected):
    data = response.json()

    def compare(actual, exp):
        for k, v in exp.items():
            actual_value = actual[k]

            if isinstance(v, str) and "T" in v:
                actual_value = normalize_datetime(actual_value)
                v = normalize_datetime(v)

            assert actual_value == v

    if isinstance(expected, list):
        assert len(data) == len(expected)
        for a, e in zip(data, expected):
            compare(a, e)
    else:
        compare(data, expected)


# =========================
# Tests - Accounts
# =========================


def test_create_account(client, monkeypatch):

    async def fake_create(account):
        return build_account(
            account_id=1,
            user_id=account.user_id,
            balance=account.balance,
        )

    monkeypatch.setattr(account_service, "create", fake_create)

    response = client.post("/accounts/", json=account_payload())

    assert response.status_code == 201

    assert_json(response, build_account(1, 1, 1000))


def test_read_accounts(client, monkeypatch):

    async def fake_read_all(limit, skip):
        return [
            build_account(1, 1, 1000),
            build_account(2, 2, 2000),
        ]

    monkeypatch.setattr(account_service, "read_all", fake_read_all)

    response = client.get("/accounts/?limit=10&skip=0")

    assert response.status_code == 200

    assert_json(
        response,
        [
            build_account(1, 1, 1000),
            build_account(2, 2, 2000),
        ],
    )


# =========================
# Tests - Transactions
# =========================


def test_read_account_transactions(client, monkeypatch):

    async def fake_read_all(account_id, limit, skip):
        return build_transaction(account_id)

    monkeypatch.setattr(tx_service, "read_all", fake_read_all)

    response = client.get("/accounts/1/transactions?limit=10&skip=0")

    assert response.status_code == 200

    assert_json(response, build_transaction(1))
