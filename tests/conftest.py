import subprocess

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.orm import clear_mappers

from api.app import app
from shopy.common.containers.main_container import MainContainer
from shopy.common.infrastructure.mappers import mappers
from shopy.user.application.container.user_container import UserContainer


@pytest_asyncio.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture()
def start_mappers():
    mappers()
    yield
    clear_mappers()


@pytest.fixture
def apply_migrations(start_mappers):
    subprocess.run(["alembic", "upgrade", "head"])
    yield
    subprocess.run(["alembic", "downgrade", "base"])


@pytest.fixture
def main_container():
    main_container = MainContainer()
    main_container.init_resources()
    return main_container


@pytest_asyncio.fixture
async def db(apply_migrations, main_container):
    db = main_container.session()

    async with db() as session:
        yield session


@pytest.fixture
def user_container():
    user_container = UserContainer()
    user_container.init_resources()
    return user_container
