import time
from collections import OrderedDict

class LRUCacheWithTTL:
    def __init__(self, capacity: int, ttl: int):
        self.capacity = capacity  # Maximum number of items in cache
        self.ttl = ttl  # TTL in seconds
        self.cache = OrderedDict()  # OrderedDict to maintain LRU order
        self.expirations = {}  # Dictionary to track expiration times

    def _is_expired(self, key: int) -> bool:
        """Check if the item has expired"""
        if key not in self.expirations:
            return False
        return time.time() > self.expirations[key]

    def _evict(self):
        """Evict the least recently used (LRU) item"""
        if self.cache:
            key, _ = self.cache.popitem(last=False)  # Remove the item from the front
            self.expirations.pop(key, None)  # Remove its expiration entry

    def _clean_expired_items(self):
        """Remove expired items from cache"""
        current_time = time.time()
        keys_to_remove = [key for key, exp_time in self.expirations.items() if exp_time < current_time]
        for key in keys_to_remove:
            if key in self.cache:
                del self.cache[key]
                del self.expirations[key]

    def get(self, key: int) -> int:
        """Retrieve the value from the cache if not expired, else return -1"""
        # Check and remove expired items before proceeding
        self._clean_expired_items()

        if key in self.cache:
            if self._is_expired(key):
                # If the item is expired, remove it and return -1
                del self.cache[key]
                del self.expirations[key]
                return -1
            else:
                # Move the item to the end (most recently used)
                self.cache.move_to_end(key)
                return self.cache[key]
        return -1

    def put(self, key: int, value: int):
        """Insert or update an item in the cache"""
        # Check and remove expired items before adding a new one
        self._clean_expired_items()

        if len(self.cache) >= self.capacity:
            self._evict()  # Evict the least recently used item if the cache is full

        # Insert or update the item
        self.cache[key] = value
        self.expirations[key] = time.time() + self.ttl  # Set the expiration time
        self.cache.move_to_end(key)  # Mark this item as the most recently used


# Example usage:
cache = LRUCacheWithTTL(3, 5)  # Capacity 3, TTL 5 seconds

cache.put(1, 100)
cache.put(2, 200)
cache.put(3, 300)

print(cache.get(1))  # Should return 100 (recently used)

time.sleep(6)  # Wait for 6 seconds, which is beyon
