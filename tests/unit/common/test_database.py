import pytest
from sqlalchemy import text  # Import the text function
from sqlalchemy.exc import SQLAlchemyError


@pytest.mark.asyncio
async def test_database_connection(db):
    try:
        # Simulate a database operation using the db fixture
        async with db as session:
            # You can execute queries or perform other operations here
            result = await session.execute(text("SELECT 1"))
            assert result.scalar() == 1
    except SQLAlchemyError as e:
        pytest.fail(f"Database connection test failed: {str(e)}")

    # After the async with block, the session should be closed
    with pytest.raises(SQLAlchemyError):
        # Attempt to use the closed session, which should raise an SQLAlchemyError
        await session.execute("SELECT 1")

    assert db.is_active is True


@pytest.mark.asyncio
async def test_database_error_handling(db):
    with pytest.raises(SQLAlchemyError):
        await db.execute(
            "INSERT INTO your_table (column) VALUES (:key)", {"key": "value"}
        )
        await db.commit()
