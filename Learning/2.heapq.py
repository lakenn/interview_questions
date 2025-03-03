import heapq
import time
from enum import Enum, auto

list = [('a', 10), ('b', 9), ('c', 8), ('d', 7)]

heapq.heapify(list)
print(list)

list2 = [(second, first) for first, second in list]
heapq.heapify(list2)
print(list2)

print(list2[0])
heapq.heappop(list2)
print(list2[0])

heapq.heappush(list2, (0, 'e'))
print(list2[0])


class BuySell(Enum):
    BUY = 'BUY'
    SELL = 'SELL'

class Order:
    def __init__(self, order_id, qty, price, buySell):
        self.order_id = order_id
        self.qty = qty
        self.price = price
        self.buySell = buySell
        self.creation_time = time.time()

    def __lt__(self, other):
        if self.price == other.price:
            return self.creation_time < other.creation_time

        return self.price < other.price if self.buySell == 'Sell' else self.price > other.price

    def __repr__(self):
        return f'Order Id: {self.order_id}-{self.buySell}-{self.price}-{self.qty}'

order1 = Order(1, 10, 100, 'Sell')
order2 = Order(2, 10, 100, 'Sell')
order3 = Order(3, 10, 90, 'Sell')

print(order1.creation_time, order2.creation_time)
orderBooks = []
heapq.heappush(orderBooks, order1)
heapq.heappush(orderBooks, order2)
heapq.heappush(orderBooks, order3)

print(heapq.heappop(orderBooks))
print(heapq.heappop(orderBooks))
print(heapq.heappop(orderBooks))

action = BuySell("BUY")

from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
print(type(Season.SPRING))
print(repr(Season.SPRING))


class Color(Enum):
    PURPLE = auto()
    RED = auto()


print(Color.PURPLE.name)