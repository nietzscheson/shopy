from typing import List

from shopy.user.domain.user import User
from shopy.user.domain.user_repository import UserRepository


class InmemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self.users = []

    def add(self, user: User) -> User:
        self.users.append(user)
        return user

    def all(self) -> List[User]:
        return self.users

    def total(self) -> int:
        return len(self.users)
