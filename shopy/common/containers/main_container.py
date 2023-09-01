from dependency_injector import containers, providers

from shopy.common.infrastructure.database import database
from shopy.common.infrastructure.unit_of_work import SqlAlchemyUnitOfWork


class MainContainer(containers.DeclarativeContainer):
    # config = providers.Configuration(pydantic_settings=[settings])

    session = providers.Resource(database.get_db)
    unit_of_work = providers.Factory(
        SqlAlchemyUnitOfWork,
        session=session,
    )
