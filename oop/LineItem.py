from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<order total: {:.2f} due:{:.2f}>'
        return fmt.format(self.total().self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""


class FidelityPromo(Promotion, ABC):
    """5% discount for customer with 1000 or more fidelity points"""


def discount(self, order):
    return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo:
    """10% discount for each line item with 20 or more units."""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total * 0.1
            return discount


class LargeOrderPromo(Promotion):
    """7% discount for orders with 10 or more distinct items."""

    def discount(self, order):
        distinct_item = {item.product for item in order.cart}

        if len(distinct_item) >= 10:
            return order.total() * 0.7
        return 0


print(y())
y = LineItem("fone", 500, 2000)


#
# datetime module
# staticmethod
