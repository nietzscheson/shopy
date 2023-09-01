import pytest
from sqlalchemy import select

from shopy.user.application.container.user_container import UserContainer
from shopy.user.application.services.create import UserCreateService
from shopy.user.domain.schemes.user_scheme import UserScheme
from shopy.user.domain.user import User
from tests.factories.user import UserFactory


@pytest.mark.asyncio
async def test_user_container(db):
    user_container = UserContainer()

    async with await user_container.main_container.unit_of_work() as uow:
        _user_factory = UserFactory.build()
        _user_scheme = UserScheme(name=_user_factory.name)

        user_service = UserCreateService(
            user_repository=await user_container.user_repository()
        )
        await user_service(user_scheme=_user_scheme)
        await uow.commit()

        query = select(User).where(User.name == _user_factory.name)

        _user = await db.execute(query.limit(1))

        assert _user_factory.name == _user.scalar().name
