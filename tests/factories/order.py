import factory

from shopy.order.domain.order import Order
from tests.factories.user import UserFactory


class OrderFactory(factory.Factory):
    class Meta:
        model = Order

    user = factory.SubFactory(UserFactory)
