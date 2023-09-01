import subprocess

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.orm import clear_mappers

from api.app import app
from shopy.common.containers.main_container import MainContainer
from shopy.common.infrastructure.mappers import mappers


@pytest_asyncio.fixture
async def client():
    # return TestClient(app)
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
def start_mappers():
    mappers()
    yield
    clear_mappers()


@pytest.fixture
def apply_migrations(start_mappers):
    subprocess.run(["alembic", "upgrade", "head"])
    yield
    subprocess.run(["alembic", "downgrade", "base"])


@pytest_asyncio.fixture
async def db(apply_migrations):
    main_container = MainContainer()

    async for session in main_container.database().get_db():
        yield session
