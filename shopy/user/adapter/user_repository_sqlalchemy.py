from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from shopy.user.domain.user import User
from shopy.user.domain.user_repository import UserRepository


class UserRepositorySQLAlchemy(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def one(self, id: str) -> User:
        query = select(User).where(User.id == id)

        result = await self.session.execute(query)

        return result.scalars().first()

    async def add(self, user: User) -> None:
        self.session.add(user)

    async def update(self, id: str, user: User) -> User:
        query = select(User).where(User.id == id)

        result = await self.session.execute(query)

        return result.scalars().first()

    async def delete(self, id: str) -> None:
        query = select(User).where(User.id == id)

        result = await self.session.execute(query)

        await self.session.delete(result.scalars().first())

    async def all(self) -> List[User]:
        query = select(User)

        result = await self.session.execute(query)

        return result.scalars().all()

    def total(self) -> int:
        return len(self.all())
