import pytest

from tests.factories.user import UserFactory


@pytest.mark.asyncio
async def test_user_create(client):
    _user = UserFactory.build()

    response = await client.post("/user", json={"name": _user.name})
    assert response.status_code == 200


#
#
# def test_get_users_1(client):
#     client.post("/user")
#     response = client.get("/users")
#     assert response.status_code == 200
#
#     assert response.json() == 1
#
#
# def test_get_users_2(client):
#     for _ in range(10):
#         client.post("/user")
#
#     response = client.get("/users")
#     assert response.status_code == 200
#
#     assert response.json() == 11
#
