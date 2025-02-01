from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        """ Return the value of the key if it exists in the cache, otherwise return -1. """
        if key not in self.cache:
            return -1
        # Move the accessed key to the end to mark it as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """ Insert or update the key-value pair in the cache. If the cache is full, evict the least recently used item. """
        if key in self.cache:
            # Update the value and move the key to the end
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            # Remove the first item (least recently used)
            self.cache.popitem(last=False)
        # Add or update the key-value pair at the end
        self.cache[key] = value


