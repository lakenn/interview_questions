"""
https://leetcode.com/discuss/interview-question/2079858/stock-exchange-lld

Stock Exchange
The Challenge


Implement an order matching system for a stock exchange. Traders place Buy and Sell orders for a stock indicating the price and quantity. Each order gets entered into the exchange’s order-book and remains there until it is matched. Order matching is attempted whenever a new order is added.


The exchange follows a FirstInFirstOut Price-Time order-matching rule, which states that: "The first order in the order-book at a price level is the first order matched. All orders at the same price level are filled according to time priority." The exchange works like a market where lower selling prices and higher buying prices get priority.


A trade is executed when a buy price is greater than or equal to a sell price. The trade is recorded at the price of the sell order regardless of the price of the buy order.


Your program should take as input:


Order ID.
Time.
Stock.
Buy/Sell.
Price.
Quantity.
The output should be


Buy Order ID
Sell Price
Quantity
Sell Order ID
Input format: <buy/sell>
Output format:


SAMPLE INPUT-OUTPUT


INPUT:
#1 09:45 BAC sell 240.12 100
#2 09:46 BAC sell 237.45 90
#3 09:47 BAC buy 238.10 110
#4 09:48 BAC buy 237.80 10
#5 09:49 BAC buy 237.80 40
#6 09:50 BAC sell 236.00 50


OUTPUT:
#3 237.45 90 #2
#3 236.00 20 #6
#4 236.00 10 #6
#5 236.00 20 #6


Input needs to be read from a text file, and output should be printed to console. Your program should execute and take the location to the test file as parameter.

You can solve this with a Map: Ticker -> OrderBook where OrderBook is a minheap and maxheap for sellOrders and buyOrders respectively.


When an order comes in, match it to an OrderBook. If it is a sale, pop the highest paying buyOrder. If there isnt one, just push the sale to the heap and return. If sale quantity exceeds buy quantity, push sellOrder to sellOrders heap. Otherwise decrement buyOrder quantity and push to buyOrders heap. In either case, append a completed trade to your output like (seller_id, price, quantity, buyer_id) with the sale price and lower quantity.
If it is a buy, pop the lowest paying sellOrder and you do the same thing as above but with the places reversed.


Adding an order is a log(n) insertion to the heap. Popping the max buyOrder or min sellOrder is O(1). Each transaction requires 1 pop. One order may trigger multiple sales, however.


Space Complexity is O(n) in the number of orders.
"""
import sys
from dataclasses import dataclass
import heapq
from datetime import datetime
from collections import defaultdict
from enum import Enum


# Enum to represent Buy and Sell
class OrderType(Enum):
    BUY = 'buy'
    SELL = 'sell'

@dataclass
class Order:
    order_id: int
    creation_time: datetime
    ticker: str
    order_type: OrderType
    price: float
    qty: float

    def __lt__(self, other):
        # same price, then compare with creation_time
        if self.price == other.price:
            return self.creation_time < other.creation_time

        # min heap for SELL order, max heap for BUY order
        return self.price < other.price if self.order_type == OrderType.SELL \
            else self.price > other.price


class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def add_order(self, order):
        if order.order_type == OrderType.BUY:
            heapq.heappush(self.buy_orders, order)
        else:
            heapq.heappush(self.sell_orders, order)
        self.match_orders()

    def match_orders(self):
        """ Try to match buy and sell orders. """
        matched_trades = []
        while self.buy_orders and self.sell_orders:
            buy_order: Order = self.buy_orders[0]
            sell_order: Order = self.sell_orders[0]

            if buy_order.price >= sell_order.price:
                # match order
                trade_quantity = min(buy_order.qty, sell_order.qty)

                # Update order quantities
                buy_order.qty -= trade_quantity
                sell_order.qty -= trade_quantity

                if buy_order.qty == 0:
                    heapq.heappop(self.buy_orders)

                if sell_order.qty == 0:
                    heapq.heappop(self.sell_orders)

                matched_trades.append(f'{buy_order.order_id} {sell_order.price} {trade_quantity} {sell_order.order_id} ')
            else:
                break

        for trade in matched_trades:
            print(trade)


class Exchange:
    def __init__(self):
        self.order_books = defaultdict(OrderBook)

    def add_order(self, stock_order: Order):
        self.order_books[stock_order.ticker].add_order(stock_order)

    def add_stock_order(self, order_id, order_type, ticker, price, qty, creation_time):
        stock_order = Order(order_id=order_id,
                            order_type=order_type,
                            ticker=ticker,
                            price=price,
                            qty=qty,
                            creation_time=creation_time)

        self.order_books[stock_order.ticker].add_order(stock_order)

def read_input(file_path):
    exchange = Exchange()
    with open(file_path, "r") as file:
        for line in file:
            order_info = line.strip().split()
            order_id = order_info[0]
            creation_time = order_info[1]
            ticker = order_info[2]
            action = order_info[3]
            price = float(order_info[4])
            qty = int(order_info[5])
            stock_order = Order(order_id=order_id,
                                order_type=OrderType(action),
                                ticker=ticker,
                                price=price,
                                qty=qty,
                                creation_time=creation_time)

            exchange.add_order(stock_order)


if __name__ == "__main__":
    # file_path = sys.argv[1]  # Take input file location as argument
    file_path = '../order_input.txt'
    read_input(file_path)

# Test the implementation
if __name__ == '__main__':
    # Instantiate the exchange
    exchange = Exchange()

    # Sample orders for different stock tickers
    exchange.add_stock_order('#1', OrderType.SELL, "AAPL", 240.12, 100, datetime(2023, 10, 1, 9, 45))
    exchange.add_stock_order('#2', OrderType.SELL, "AAPL", 237.45, 90, datetime(2023, 10, 1, 9, 46))
    exchange.add_stock_order('#3', OrderType.BUY, "AAPL", 238.10, 110, datetime(2023, 10, 1, 9, 47))
    exchange.add_stock_order('#4',OrderType.BUY, "AAPL", 237.80, 10, datetime(2023, 10, 1, 9, 48))
    exchange.add_stock_order('#5', OrderType.BUY, "AAPL", 237.80, 40, datetime(2023, 10, 1, 9, 49))
    exchange.add_stock_order('#6', OrderType.SELL, "AAPL", 236.00, 50, datetime(2023, 10, 1, 9, 50))
    #
    # Add orders for another ticker (e.g., MSFT)
    exchange.add_stock_order('#7', OrderType.BUY, "MSFT", 150.00, 200, datetime(2023, 10, 1, 9, 45))
    exchange.add_stock_order('#8', OrderType.SELL, "MSFT", 145.00, 150, datetime(2023, 10, 1, 9, 46))
    exchange.add_stock_order('#9', OrderType.SELL, "MSFT", 149.00, 50, datetime(2023, 10, 1, 9, 47))

    # Now, for the AAPL ticker, the orders will be matched according to FIFO and price priority.