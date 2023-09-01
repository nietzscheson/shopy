from sqlalchemy import Column, String, Table
from sqlalchemy.dialects.postgresql import UUID

from shopy.common.infrastructure.mapper_registry import mapper_registry

users_table = Table(
    "users",
    mapper_registry.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True),
    Column("name", String, index=True),
)
