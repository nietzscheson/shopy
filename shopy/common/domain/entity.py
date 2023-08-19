import uuid
from dataclasses import dataclass, field


@dataclass
class Entity:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
