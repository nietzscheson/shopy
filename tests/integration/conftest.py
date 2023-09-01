import pytest

from shopy.common.infrastructure.unit_of_work import SqlAlchemyUnitOfWork


@pytest.fixture
def unit_of_work(db):
    return SqlAlchemyUnitOfWork(db)
