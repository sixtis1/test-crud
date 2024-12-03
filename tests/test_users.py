import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.dependencies import get_user_repository
from app.repositories.memory_repository import MemoryUserRepository


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
def memory_repository():
    return MemoryUserRepository()


@pytest.fixture
def override_get_user_repository(memory_repository):
    async def _override():
        yield memory_repository

    return _override


@pytest.fixture(autouse=True)
def setup_dependency_overrides(override_get_user_repository):
    app.dependency_overrides[get_user_repository] = override_get_user_repository
    yield
    app.dependency_overrides.clear()


@pytest.fixture
async def client() -> AsyncClient:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://testserver"
    ) as ac:
        yield ac


@pytest.mark.anyio
async def test_create_user(client: AsyncClient):
    response = await client.post("/users/", json={"full_name": "John Doe"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["full_name"] == "John Doe"


@pytest.mark.anyio
async def test_get_user(client: AsyncClient):
    response = await client.post("/users/", json={"full_name": "Jane Doe"})
    assert response.status_code == 200
    user_id = response.json()["id"]

    response = await client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["full_name"] == "Jane Doe"


@pytest.mark.anyio
async def test_update_user(client: AsyncClient):
    response = await client.post("/users/", json={"full_name": "John Smith"})
    assert response.status_code == 200
    user_id = response.json()["id"]

    response = await client.put(f"/users/{user_id}", json={"full_name": "John Doe"})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["full_name"] == "John Doe"


@pytest.mark.anyio
async def test_delete_user(client: AsyncClient):
    response = await client.post("/users/", json={"full_name": "John Doe"})
    assert response.status_code == 200
    user_id = response.json()["id"]

    response = await client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "User deleted successfully"

    response = await client.get(f"/users/{user_id}")
    assert response.status_code == 404
