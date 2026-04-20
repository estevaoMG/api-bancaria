from contextlib import asynccontextmanager

import pytest
from fastapi import APIRouter
from fastapi.testclient import TestClient

from src.exceptions import AccountNotFoundError, BusinessError
from src.main import app


# 🔹 Override do lifespan (evita conexão com banco)
@asynccontextmanager
async def lifespan_override(app):
    yield


@pytest.fixture
def client():
    app.router.lifespan_context = lifespan_override
    with TestClient(app) as client:
        yield client


# ✅ App sobe corretamente
def test_app_startup(client):
    response = client.get("/docs")
    assert response.status_code == 200


# ✅ OpenAPI válido
def test_openapi_schema(client):
    response = client.get("/openapi.json")

    assert response.status_code == 200
    data = response.json()

    assert "openapi" in data
    assert "paths" in data


# ✅ CORS funcionando (preflight)
def test_cors_preflight(client):
    response = client.options(
        "/accounts/",
        headers={
            "Origin": "http://localhost",
            "Access-Control-Request-Method": "POST",
        },
    )

    assert response.status_code in [200, 204]
    assert "access-control-allow-origin" in response.headers


# ✅ Rota inexistente
def test_not_found_route(client):
    response = client.get("/rota-inexistente")

    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"


# ✅ Handler AccountNotFoundError
def test_account_not_found_handler(client):
    router = APIRouter()

    @router.get("/test-account-error")
    async def fake():
        raise AccountNotFoundError()

    app.include_router(router)

    response = client.get("/test-account-error")

    assert response.status_code == 404
    assert response.json() == {"detail": "Account not found."}


# ✅ Handler BusinessError
def test_business_error_handler(client):
    router = APIRouter()

    @router.get("/test-business-error")
    async def fake():
        raise BusinessError("Erro de negócio")

    app.include_router(router)

    response = client.get("/test-business-error")

    assert response.status_code == 409
    assert response.json() == {"detail": "Erro de negócio"}
