from dependency_injector import containers, providers

from shopy.common.infrastructure.database import Database
from shopy.common.infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from shopy.common.settings import Settings


class MainContainer(containers.DeclarativeContainer):
    config = providers.Singleton(Settings)

    database = providers.Singleton(Database, database_uri=config().DATABASE_URI)

    session = providers.Resource(database.provided.get_db)
    unit_of_work = providers.Factory(
        SqlAlchemyUnitOfWork,
        session=session,
    )
