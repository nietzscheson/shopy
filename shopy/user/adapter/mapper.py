from sqlalchemy.orm import registry

from shopy.user.adapter.user_table import users_table
from shopy.user.domain.user import User

mapper_registry = registry()

mapper_registry.map_imperatively(User, users_table)
