import pytest
from sqlalchemy import select

from shopy.user.domain.user import User
from tests.factories.user import UserFactory


@pytest.mark.asyncio
@pytest.mark.debug
async def test_user_create(client, apply_migrations, db):
    _user_factory = UserFactory.build()

    response = await client.post("/user", json={"name": _user_factory.name})

    data = response.json()
    assert response.status_code == 200
    assert data["name"] == _user_factory.name

    query = select(User)

    resultado = await db.execute(query)

    assert _user_factory.name == resultado.scalars().all()[0].name
