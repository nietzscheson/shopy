from typing import Any

from shopy.user.domain.schemes.user_scheme import UserScheme
from shopy.user.domain.user import User
from shopy.user.domain.user_repository import UserRepository


class UserCreateService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    async def __call__(self, user_scheme: UserScheme) -> Any:
        _user = User(
            name=user_scheme.name,
        )
        await self.user_repository.add(_user)
