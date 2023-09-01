import pytest

from shopy.common.infrastructure.unit_of_work import SqlAlchemyUnitOfWork


@pytest.mark.asyncio
async def test_aenter(unit_of_work):
    async with unit_of_work as uow:
        assert uow is not None


@pytest.mark.asyncio
async def test_aexit(unit_of_work):
    async with unit_of_work:
        pass


@pytest.mark.asyncio
async def test_commit(unit_of_work):
    # ToDo:
    #   some_model_instance = SomeModel(data="test")
    #   db.add(some_model_instance)
    await unit_of_work._commit()

    # With another session or the same to check if the data was actually committed.
    # For the sake of this example, we're just verifying that no errors occurred during commit.


@pytest.mark.asyncio
async def test_rollback(db):
    unit_of_work = SqlAlchemyUnitOfWork(db)

    ## ToDo
    # Perform some operations here like adding to the db
    # Then rollback and check if the database remains unaffected.

    # Just a dummy operation for this example:
    #   some_model_instance = SomeModel(data="test")
    #   db.add(some_model_instance)
    await unit_of_work.rollback()

    # Validate that the data wasn't added to the database.
