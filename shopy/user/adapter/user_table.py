from sqlalchemy import Column, Integer, MetaData, String, Table

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, index=True),
)
