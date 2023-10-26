from contextlib import AbstractAsyncContextManager
from typing import Callable, Iterator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from shopy.common.domain.unit_of_work import AbstractUnitOfWork


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(
        self, session: Callable[..., AbstractAsyncContextManager[AsyncSession]]
    ) -> None:
        self.session_factory = session()
        self.session = None

    async def __aenter__(self):
        enter = await super().__aenter__()

        async with self.session_factory as session:
            self.session = session
        return enter
        # async with self.session_factory as session:
        #    self.session = session
        #    print(self.session)
        #    yield await session

    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        async with self.session as session:
            await session.close()

    async def commit(self):
        print("Commit Session", self.session)
        await self.session.commit()


#    async def _commit(self):
#        print("UnitOfWork",self.session)
#        async with self.session as session:
#            await session.commit()
#        #async with self.session as session:
#        #    print("Committing session", session)
#        #    await session.commit()  # Manual commit if needed
#
#    async def rollback(self):
#        async with self.session as session:
#            session.rollback()
#
