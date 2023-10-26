import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

logger = logging.getLogger(__name__)


class Database:
    def __init__(self, database_uri: str, echo_sql: bool = False) -> None:
        self.__async_engine = create_async_engine(
            database_uri,
            max_overflow=10,
            pool_size=10,
            pool_recycle=900,
            pool_timeout=30,
            # pool_pre_ping=True,
            echo=echo_sql,
        )

        self.__AsyncSessionLocal = async_sessionmaker(
            bind=self.__async_engine,
            autoflush=False,
            expire_on_commit=False,
        )

    @asynccontextmanager
    async def get_db(
        self,
    ) -> AsyncGenerator[AsyncSession, None]:
        db: AsyncSession = self.__AsyncSessionLocal()
        try:
            yield db
        except Exception as e:
            logger.error(e)
            await db.rollback()
            raise SQLAlchemyError(
                status_code=500, detail=f"Error in the Database: {str(e)}"
            )
        finally:
            await db.close()

    @asynccontextmanager
    async def connection(
        self,
    ):
        connection = self.__async_engine.connect()
        async with connection as connection:
            yield connection
            await connection.close()
