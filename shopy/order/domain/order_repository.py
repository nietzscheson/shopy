import abc
from typing import List

from shopy.order.domain.order import Order


class OrderRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, user: Order) -> Order:
        raise NotImplementedError

    @abc.abstractmethod
    def all(self) -> List[Order]:
        raise NotImplementedError

    @abc.abstractmethod
    def total(self) -> int:
        raise NotImplementedError
