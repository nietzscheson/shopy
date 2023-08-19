import factory

from shopy.product.domain.product import Product
from tests.factories.user import UserFactory


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    title = factory.Faker("name")
    user = factory.SubFactory(UserFactory)
