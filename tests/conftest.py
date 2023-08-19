import pytest
from starlette.testclient import TestClient


@pytest.fixture
def client():
    from api.app import app

    return TestClient(app)
