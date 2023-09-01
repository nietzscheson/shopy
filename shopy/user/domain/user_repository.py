import abc
from typing import List

from shopy.user.domain.user import User


class UserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def one(self, id: str) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, user: User) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, id: str, user: User) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def all(self) -> List[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def total(self) -> int:
        raise NotImplementedError
