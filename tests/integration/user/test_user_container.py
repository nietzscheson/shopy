import pytest
from sqlalchemy import select

from shopy.user.application.container.user_container import UserContainer
from shopy.user.application.services.create import UserCreateService
from shopy.user.domain.schemes.user_scheme import UserScheme
from shopy.user.domain.user import User
from tests.factories.user import UserFactory


@pytest.mark.asyncio
@pytest.mark.debug
async def test_user_container(apply_migrations, user_container):
    # user_container = UserContainer()
    db = await user_container.main_container.session()

    unit_of_work = await user_container.main_container.unit_of_work()
    async with unit_of_work as uow:
        _user_factory = UserFactory.build()
        _user_scheme = UserScheme(name=_user_factory.name)

        user_create_service = UserCreateService(
            user_repository=await user_container.user_repository()
        )
        await user_create_service(user_scheme=_user_scheme)
        await uow.commit()

        query = select(User)

        resultado = await db.execute(query)

        assert _user_factory.name == resultado.scalars().all()[0].name
