from contextlib import asynccontextmanager

import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.security import get_current_user


# Mock do lifespan (não conecta no banco real)
@asynccontextmanager
async def test_lifespan(app):
    yield


# Mock de usuário autenticado
def override_get_current_user():
    return {"id": 1, "username": "test"}


@pytest.fixture
def client():
    app.router.lifespan_context = test_lifespan
    app.dependency_overrides[get_current_user] = override_get_current_user
    return TestClient(app)
