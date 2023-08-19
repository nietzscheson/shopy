from typing import List

from shopy.product.domain.product import Product
from shopy.product.domain.product_repository import ProductRepository


class InmemoryProductRepository(ProductRepository):
    def __init__(self) -> None:
        self.products = []

    def add(self, product: Product) -> Product:
        self.products.append(product)
        return product

    def all(self) -> List[Product]:
        return self.products

    def total(self) -> int:
        return len(self.products)
