def test_get_users_0(client):
    response = client.get("/users")
    assert response.status_code == 200


def test_get_users_1(client):
    client.post("/user")
    response = client.get("/users")
    assert response.status_code == 200

    assert response.json() == 1


def test_get_users_2(client):
    for _ in range(10):
        client.post("/user")

    response = client.get("/users")
    assert response.status_code == 200

    assert response.json() == 11
