import time
import heapq

class ExpiringKeyValueStore:
    def __init__(self):
        self.store = {}  # Dictionary to hold the key-value pairs
        self.expiry_heap = []  # Min-heap to efficiently access the key with the earliest expiry time

    def set(self, key, value, ttl):
        """
        Sets a key-value pair with a Time-To-Live (TTL) in seconds.
        The key will expire after ttl seconds.
        """
        expiry_time = time.time() + ttl
        self.store[key] = value
        # Push the (expiry_time, key) tuple into the min-heap
        heapq.heappush(self.expiry_heap, (expiry_time, key))

    def get(self, key):
        """
        Gets the value associated with a key if it is still valid.
        Returns None if the key is expired or does not exist.
        """
        self._cleanup_expired()
        return self.store.get(key, None)

    def _cleanup_expired(self):
        """
        Removes expired keys from the store by checking the min-heap and timestamps.
        """
        now = time.time()
        while self.expiry_heap and self.expiry_heap[0][0] < now:
            # Pop the earliest expiring key from the heap
            _, key = heapq.heappop(self.expiry_heap)
            # Remove the key if it's expired
            if key in self.store:
                del self.store[key]

    def remove(self, key):
        """
        Removes a key from the store immediately.
        """
        if key in self.store:
            del self.store[key]
            # Also remove from the heap (this is not efficient in this version)
            self.expiry_heap = [(expiry_time, k) for expiry_time, k in self.expiry_heap if k != key]
            heapq.heapify(self.expiry_heap)

    def __str__(self):
        """
        Returns a string representation of the current store.
        """
        return str(self.store)

# Example Usage:

kv_store = ExpiringKeyValueStore()

# Set keys with TTL
kv_store.set("key1", "value1", ttl=5)  # Expires in 5 seconds
kv_store.set("key2", "value2", ttl=10)  # Expires in 10 seconds

# Wait for 3 seconds
time.sleep(3)

# Get values
print(kv_store.get("key1"))  # Should return "value1"
print(kv_store.get("key2"))  # Should return "value2"

# Wait for 3 more seconds (total 6 seconds for key1)
time.sleep(3)

# Get values after expiry of key1
print(kv_store.get("key1"))  # Should return None, as it's expired
print(kv_store.get("key2"))  # Should return "value2", as it hasn't expired yet
