from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from shopy.common.domain.entity import Entity
from shopy.user.domain.user import User

if TYPE_CHECKING:
    from shopy.order.domain.order_repository import OrderRepository


@dataclass
class Order(Entity):
    user: User = field(default=User())

    def save(self, repository: "OrderRepository"):
        return repository.add(self)

    def __hash__(self):
        return hash(self.id)
