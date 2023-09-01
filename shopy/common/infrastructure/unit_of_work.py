from shopy.common.domain.unit_of_work import AbstractUnitOfWork


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session):
        self.session = session

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def _commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
