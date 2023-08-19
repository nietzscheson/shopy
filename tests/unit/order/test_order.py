import uuid

from shopy.order.domain.order import Order
from tests.factories.user import UserFactory


def test_order():
    id = str(uuid.uuid4())

    user = UserFactory.build(id=id)

    order = Order(id=id, user=user)

    assert order.id == id
    assert order.user.id == id
    assert order.user.name == user.name


def test_order_default():
    id = str(uuid.uuid4())

    assert Order().id != id
