from shopy.product.adapter.inmemory_product_repository import InmemoryProductRepository
from shopy.product.domain.product import Product


def test_product_repository_all():
    product_repository = InmemoryProductRepository()

    product_1 = Product().save(product_repository)
    product_2 = Product().save(product_repository)

    assert set(product_repository.all()) == {product_1, product_2}
