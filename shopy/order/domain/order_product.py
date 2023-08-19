from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from shopy.common.domain.entity import Entity
from shopy.order.domain.order import Order
from shopy.product.domain.product import Product

if TYPE_CHECKING:
    from shopy.order.domain.order_product_repository import OrderProductRepository


@dataclass
class OrderProduct(Entity):
    order: Order = field(default=Order())
    product: Product = field(default=Product())
    price: float = field(default=0.0)
    quantity: float = field(default=0)

    def save(self, repository: "OrderProductRepository"):
        return repository.add(self)

    def __hash__(self):
        return hash(self.id)
