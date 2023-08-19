import uuid

from shopy.product.domain.product import Product
from tests.factories.user import UserFactory


def test_product():
    id = str(uuid.uuid4())

    user = UserFactory.build(id=id)

    product = Product(id=id, title="The Product", user=user)

    assert product.id == id
    assert product.title == "The Product"
    assert product.user.id == id
    assert product.user.name == user.name


def test_product_default():
    id = str(uuid.uuid4())

    assert Product().id != id
