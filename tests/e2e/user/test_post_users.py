def test_post_user(client):
    response = client.post("/user")
    assert response.status_code == 200
