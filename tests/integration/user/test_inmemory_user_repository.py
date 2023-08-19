from shopy.user.adapter.inmemory_user_repository import InmemoryUserRepository
from shopy.user.domain.user import User


def test_user_repository_all():
    user_repository = InmemoryUserRepository()

    user_1 = User().save(user_repository)
    user_2 = User().save(user_repository)

    assert set(user_repository.all()) == {user_1, user_2}
