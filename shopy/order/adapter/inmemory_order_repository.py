from typing import List

from shopy.order.domain.order import Order
from shopy.order.domain.order_repository import OrderRepository


class InmemoryOrderRepository(OrderRepository):
    def __init__(self) -> None:
        self.orders = []

    def add(self, order: Order) -> Order:
        self.orders.append(order)
        return order

    def all(self) -> List[Order]:
        return self.orders

    def total(self) -> int:
        return len(self.orders)
