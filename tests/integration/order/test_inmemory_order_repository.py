from shopy.order.adapter.inmemory_order_repository import InmemoryOrderRepository
from shopy.order.domain.order import Order


def test_order_repository_all():
    order_repository = InmemoryOrderRepository()

    _1 = Order().save(order_repository)
    _2 = Order().save(order_repository)

    assert set(order_repository.all()) == {_1, _2}
