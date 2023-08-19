import factory

from shopy.user.domain.user import User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    name = factory.Faker("name")
