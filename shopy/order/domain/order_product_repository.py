import abc
from typing import List

from shopy.order.domain.order_product import OrderProduct


class OrderProductRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, user: OrderProduct) -> OrderProduct:
        raise NotImplementedError

    @abc.abstractmethod
    def all(self) -> List[OrderProduct]:
        raise NotImplementedError

    @abc.abstractmethod
    def total(self) -> int:
        raise NotImplementedError
