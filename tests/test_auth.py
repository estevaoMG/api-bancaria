import datetime

from src.controllers import account as account_controller


def test_create_account(client, monkeypatch):
    """
    Testa criação de conta com mock do service
    """

    async def fake_create(account):
        return {
            "id": 1,
            "user_id": account.user_id,
            "balance": account.balance,
            "created_at": datetime.datetime.now(datetime.timezone.utc),
        }

    monkeypatch.setattr(
        account_controller.account_service,
        "create",
        fake_create,
    )

    payload = {
        "user_id": 1,
        "balance": 1000,
    }

    response = client.post("/accounts/", json=payload)

    assert response.status_code in (200, 201)

    data = response.json()

    # validação completa
    assert data["id"] == 1
    assert data["user_id"] == 1
    assert data["balance"] == 1000

    # validação de formato (mais forte)
    assert "created_at" in data
    assert isinstance(data["created_at"], str)
