from dependency_injector import containers, providers

from shopy.common.containers.main_container import MainContainer
from shopy.user.adapter.user_repository_sqlalchemy import UserRepositorySQLAlchemy


class UserContainer(containers.DeclarativeContainer):
    main_container = providers.Container(MainContainer)

    user_repository = providers.Factory(
        UserRepositorySQLAlchemy,
        session=main_container.session,
    )
