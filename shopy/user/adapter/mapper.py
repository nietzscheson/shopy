from shopy.user.adapter.user_table import users_table
from shopy.user.domain.user import User


def mapper(mapper_registry):
    mapper_registry.map_imperatively(User, users_table)
