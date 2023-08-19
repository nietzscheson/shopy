from shopy.user.adapter.inmemory_user_repository import InmemoryUserRepository
from shopy.user.domain.user import User


def main():
    user_repository = InmemoryUserRepository()

    User().save(user_repository)
    User().save(user_repository)

    print(user_repository.all())

    print(f"Total users: ${user_repository.all()}")


if __name__ == "__main__":
    main()
