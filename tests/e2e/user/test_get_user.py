import pytest

from tests.factories.user import UserFactory


@pytest.mark.asyncio
async def test_user_create(client, apply_migrations):
    _user = UserFactory.build()

    response = await client.post("/user", json={"name": _user.name})
    print(response.json())
    # assert response.status_code == 200
