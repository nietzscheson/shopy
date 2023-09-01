import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from shopy.common.containers.main_container import MainContainer
from shopy.common.domain.unit_of_work import AbstractUnitOfWork


@pytest.mark.asyncio
async def test_main_container_session():
    container = MainContainer()

    session = await container.session()
    assert isinstance(session, AsyncSession)


@pytest.mark.asyncio
async def test_main_container_uow():
    container = MainContainer()

    unit_of_work = await container.unit_of_work()

    async with unit_of_work as uow:
        assert isinstance(uow, AbstractUnitOfWork)
