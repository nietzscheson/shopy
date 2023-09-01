from shopy.common.infrastructure.mapper_registry import mapper_registry
from shopy.user.adapter.mapper import mapper as user_mapper


def mappers():
    user_mapper(mapper_registry)
    return mapper_registry
