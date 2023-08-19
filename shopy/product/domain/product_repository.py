import abc
from typing import List

from shopy.product.domain.product import Product


class ProductRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, user: Product) -> Product:
        raise NotImplementedError

    @abc.abstractmethod
    def all(self) -> List[Product]:
        raise NotImplementedError

    @abc.abstractmethod
    def total(self) -> int:
        raise NotImplementedError
