from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from shopy.common.domain.entity import Entity

if TYPE_CHECKING:
    from shopy.user.domain.user_repository import UserRepository


@dataclass
class User(Entity):
    name: str = field(default="")

    def save(self, repository: "UserRepository"):
        return repository.add(self)

    def __hash__(self):
        return hash(self.id)
