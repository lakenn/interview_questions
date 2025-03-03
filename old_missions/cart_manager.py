from collections import defaultdict


class Cart:
    def __init__(self, cart_id: str):
        self.cart_id = cart_id
        self.items = defaultdict(int)  # Store items (item_name -> quantity)
        self.is_checked_out = False
        self.is_cancelled = False
        self.actions = []  # Store actions with their timestamps

    def add_item(self, item: str, timestamp: int) -> None:
        if self.is_cancelled:
            print(f"Cannot add items to a canceled cart: {self.cart_id}")
            return
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
        self.actions.append(("ADD_ITEM", item, timestamp))

    def remove_item(self, item: str, timestamp: int) -> None:
        if self.is_cancelled:
            print(f"Cannot remove items from a canceled cart: {self.cart_id}")
            return

        self.items[item] -= 1
        self.actions.append(("REMOVE_ITEM", item, timestamp))

    def cancel(self, timestamp: int) -> None:
        self.is_cancelled = True
        self.items.clear()  # Clear all items when canceled
        self.actions.append(("CANCEL", None, timestamp))

    def checkout(self, timestamp: int) -> None:
        if self.is_cancelled:
            print(f"Cannot checkout a canceled cart: {self.cart_id}")
            return
        self.is_checked_out = True
        self.actions.append(("CHECKOUT", None, timestamp))

    def __str__(self):
        return f"Cart {self.cart_id}: {self.items}, Checked Out: {self.is_checked_out}, Cancelled: {self.is_cancelled}, Actions: {self.actions}"


class CartManager:
    def __init__(self):
        self.carts = {}

    def process_log_line(self, log_line: str) -> None:
        log_data = log_line.strip().split(',')
        timestamp = int(log_data[0])  # Convert timestamp to integer
        cart_id = log_data[1]
        action = log_data[2]
        item = log_data[3] if len(log_data) > 3 else None

        cart = self.get_cart(cart_id)

        if action == "ADD_ITEM":
            cart.add_item(item, timestamp)
        elif action == "REMOVE_ITEM":
            cart.remove_item(item, timestamp)
        elif action == "CANCEL":
            cart.cancel(timestamp)
        elif action == "CHECKOUT":
            cart.checkout(timestamp)
        else:
            print(f"Unknown action: {action}")

    def get_cart(self, cart_id: str) -> "Cart":
        if cart_id not in self.carts:
            self.carts[cart_id] = Cart(cart_id)
        return self.carts[cart_id]

    def get_pending_carts(self):
        return [cart for cart in self.carts.values() if not cart.is_checked_out and not cart.is_cancelled]


import csv
from typing import List


class CartManager:
    def __init__(self):
        self.carts = {}  # Stores carts by cart_id

    def process_log_line(self, log_line: str) -> None:
        # Parse the log line (timestamp, cart_id, action, item)
        log_data = log_line.strip().split(',')
        timestamp = log_data[0]
        cart_id = log_data[1]
        action = log_data[2]
        item = log_data[3] if len(log_data) > 3 else None  # No item for CANCEL/ CHECKOUT

        # Get the cart or create it
        cart = self.get_cart(cart_id)

        # Handle actions
        if action == "ADD_ITEM":
            cart.add_item(item)
        elif action == "REMOVE_ITEM":
            cart.remove_item(item)
        elif action == "CANCEL":
            cart.cancel()
        elif action == "CHECKOUT":
            cart.checkout()
        else:
            print(f"Unknown action: {action}")

    def get_cart(self, cart_id: str) -> "Cart":
        if cart_id not in self.carts:
            self.carts[cart_id] = Cart(cart_id)
        return self.carts[cart_id]

    def get_pending_carts(self) -> List["Cart"]:
        return [cart for cart in self.carts.values() if not cart.is_checked_out]


class Cart:
    def __init__(self, cart_id: str):
        self.cart_id = cart_id
        self.items = {}  # Store items (item_name -> quantity)
        self.is_checked_out = False
        self.is_cancelled = False

    def add_item(self, item: str) -> None:
        if self.is_cancelled:
            print(f"Cannot add items to a canceled cart: {self.cart_id}")
            return
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def remove_item(self, item: str) -> None:
        if self.is_cancelled:
            print(f"Cannot remove items from a canceled cart: {self.cart_id}")
            return
        if item in self.items:
            if self.items[item] > 1:
                self.items[item] -= 1
            else:
                del self.items[item]

    def cancel(self) -> None:
        self.is_cancelled = True
        self.items.clear()  # Clear all items when canceled

    def checkout(self) -> None:
        if self.is_cancelled:
            print(f"Cannot checkout a canceled cart: {self.cart_id}")
            return
        self.is_checked_out = True

    def __str__(self):
        return f"Cart {self.cart_id}: {self.items}, Checked Out: {self.is_checked_out}, Cancelled: {self.is_cancelled}"


# Example usage

cart_manager = CartManager()

# Example log lines with actions
log_lines = [
    "1701971917058,cart-xb4q5x,ADD_ITEM,Coffee",
    "1701972721344,cart-xb4q5x,REMOVE_ITEM,Coffee",
    "1701975613439,cart-xb4q5x,ADD_ITEM,Coffee",
    "1705348452703,cart-7g5tgv,ADD_ITEM,Coffee",
    "1705350787970,cart-7g5tgv,REMOVE_ITEM,Coffee",
    "1702981773603,cart-m7rm8i,ADD_ITEM,Coffee",
    "1703002055655,cart-m7rm8i,ADD_ITEM,Coffee",
    "1703017798566,cart-m7rm8i,REMOVE_ITEM,Coffee",
    "1703548799784,cart-1liywk,ADD_ITEM,Coffee",
    "1703548799893,cart-1liywk,REMOVE_ITEM,Coffee",
    "1703806737183,cart-1c5729,ADD_ITEM,Coffee",
    "1703807701313,cart-1c5729,ADD_ITEM,Coffee",
    "1703808799999,cart-1c5729,CANCEL,,",  # CANCEL action
    "1703808801111,cart-1c5729,CHECKOUT,,"  # CHECKOUT action
]

# Process each log line
for log_line in log_lines:
    cart_manager.process_log_line(log_line)

# Retrieve and print the carts after processing
for cart_id, cart in cart_manager.carts.items():
    print(cart)
