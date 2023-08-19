import uuid

from shopy.order.domain.order_product import OrderProduct
from tests.factories.order import OrderFactory
from tests.factories.product import ProductFactory
from tests.factories.user import UserFactory


def test_order_product():
    id = str(uuid.uuid4())

    user = UserFactory.build(id=id)
    order = OrderFactory.build(id=id, user=user)
    product = ProductFactory.build(id=id, user=user)

    order_product = OrderProduct(
        id=id, order=order, product=product, price=15.0, quantity=3
    )

    assert order_product.id == id
    assert order_product.price == 15.0
    assert order_product.quantity == 3
    assert order_product.order.id == id
    assert order_product.product.id == id


def test_order_product_default():
    id = str(uuid.uuid4())

    assert OrderProduct().id != id
