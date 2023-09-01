import logging
from typing import AsyncGenerator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from shopy.common.settings import settings

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, database_uri: str, echo_sql: bool = False) -> None:
        self.__async_engine = create_async_engine(
            database_uri,
            # pool_pre_ping=True,
            # echo=settings.ECHO_SQL,
        )

        self.__AsyncSessionLocal = async_sessionmaker(
            bind=self.__async_engine,
            autoflush=False,
            # future=True,
            expire_on_commit=False,
        )

    async def get_db(
        self,
    ) -> AsyncGenerator[AsyncSession, None]:
        db = self.__AsyncSessionLocal()
        try:
            yield db

            await db.close()
            await self.__async_engine.dispose()

        except Exception as e:
            logger.error(e)
            await db.rollback()
            raise SQLAlchemyError(
                status_code=500, detail=f"Error in the Database: {str(e)}"
            )


database = Database(database_uri=settings.DATABASE_URI)


# AsyncSession = Annotated[async_sessionmaker, Depends(Database.get_db)]
