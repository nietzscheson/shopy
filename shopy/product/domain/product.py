from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from shopy.common.domain.entity import Entity
from shopy.user.domain.user import User

if TYPE_CHECKING:
    from shopy.product.domain.product_repository import ProductRepository


@dataclass
class Product(Entity):
    title: str = field(default="")
    price: float = field(default=0.0)
    quantity: float = field(default=0)
    user: User = field(default=User())

    def save(self, repository: "ProductRepository"):
        return repository.add(self)

    def __hash__(self):
        return hash(self.id)
