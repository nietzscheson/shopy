import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from shopy.user.adapter.user_repository_sqlalchemy import UserRepositorySQLAlchemy
from tests.factories.user import UserFactory


@pytest.mark.asyncio
async def test_user_sqlalchemy_repository_add_and_one(db: AsyncSession):
    user_repository = UserRepositorySQLAlchemy(session=db)

    user = UserFactory.create()

    await user_repository.add(user)

    await db.commit()

    _user = await user_repository.one(id=user.id)

    assert _user.name == user.name


@pytest.mark.asyncio
async def test_user_sqlalchemy_repository_add_and_update(db: AsyncSession):
    user_repository = UserRepositorySQLAlchemy(session=db)

    user = UserFactory.create()

    await user_repository.add(user)

    await db.commit()

    _user = await user_repository.one(id=user.id)

    assert _user.name == user.name

    _user.name = "Isabella"

    _user = await user_repository.update(id=user.id, user=_user)

    await db.commit()

    assert _user.name == "Isabella"


@pytest.mark.asyncio
async def test_user_sqlalchemy_repository_all(db: AsyncSession):
    user_repository = UserRepositorySQLAlchemy(session=db)

    assert len(await user_repository.all()) == 0

    [await user_repository.add(user) for user in UserFactory.create_batch(10)]

    await db.commit()

    assert len(await user_repository.all()) == 10


@pytest.mark.asyncio
async def test_user_sqlalchemy_repository_add_and_delete(db: AsyncSession):
    user_repository = UserRepositorySQLAlchemy(session=db)

    assert len(await user_repository.all()) == 0

    user = UserFactory.create()

    await user_repository.add(user)

    await db.commit()

    _user = await user_repository.one(id=user.id)

    assert _user.name == user.name

    assert len(await user_repository.all()) == 1

    await user_repository.delete(id=_user.id)

    await db.commit()

    assert len(await user_repository.all()) == 0
