from collections import defaultdict
import bisect





class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value, timestamp: int):
        # since the set is strictly increasing, we can always append to the end
        # self.store[key].append((timestamp, value))

        # if not strictly inc , we need to insert to the right pos or update the value with same timestamp
        lst = self.store[key]

        # find the right insertion pos
        idx = bisect.bisect_right(lst, timestamp, key=lambda x: x[0])

        # check if there is a value with the same timestamp
        if idx > 0 and lst[idx-1][0] == timestamp:
            lst[idx-1] = (timestamp, value)

        else:
            lst.insert(idx, (timestamp, value))
    def get(self, key: str, timestamp: int):
        lst = self.store.get(key)

        if lst:
            # Use bisect to find the right index
            # idx = bisect.bisect_right(lst, (timestamp, chr(127))) - 1  # Using a character that is greater than any valid value
            idx = bisect.bisect_right(lst, timestamp, key=lambda x: x[0]) - 1
            return lst[idx][1] if idx >= 0 else ''

        return ''



store = TimeMap()
store.set('a', 'a1', 1)
store.set('a', 'a2', 4)
store.set('a', 'a3', 8)

# Test 1: Basic Set & Get
store.set("foo", "bar", 1)
assert store.get("foo", 1) == "bar"  # Exact timestamp match

# Test 2: Getting a value at a later timestamp
assert store.get("foo", 2) == "bar"  # Should return latest value <= 2

# Test 3: Updating the value at a later timestamp
store.set("foo", "bar2", 4)
assert store.get("foo", 4) == "bar2"  # Exact match
assert store.get("foo", 3) == "bar"  # Still return the older value

# Test 4: Getting a value before any key exists
assert store.get("foo", 0) == ""  # No value exists at this timestamp

# Test 5: Setting multiple keys
store.set("key1", "val1", 5)
store.set("key1", "val2", 10)
assert store.get("key1", 7) == "val1"  # Latest <= 7
assert store.get("key1", 10) == "val2"  # Exact match

# Test 6: Querying for non-existent keys
assert store.get("unknown", 5) == ""  # No such key stored

# Test 7: Edge case - Multiple values at same timestamp
store.set("foo", "bar3", 4)  # Overwrites "bar2" at timestamp 4
assert store.get("foo", 4) == "bar3"

print("All tests passed!")


from sortedcontainers import SortedList


class TimeMap:
    def __init__(self):
        """Initialize the data structure."""
        self.store = defaultdict(SortedList)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Store the key-value pair along with the timestamp."""
        self.store[key].add((timestamp, value))  # Automatically keeps it sorted

    def get(self, key: str, timestamp: int) -> str:
        """Retrieve the latest value for the given key with timestamp ≤ given timestamp."""
        if key not in self.store:
            return ""  # Key does not exist

        values = self.store[key]
        idx = values.bisect_right((timestamp, chr(127))) - 1  # Binary search for position

        return values[idx][1] if idx >= 0 else ""  # Return found value or "" if no valid timestamp



# Example Usage
time_map = TimeMap()
time_map.set("foo", "bar", 1)
time_map.set("foo", "bar2", 4)
time_map.set("foo", "bar3", 0)  # Insert at the beginning

print(time_map.get("foo", 1))  # Output: "bar"
print(time_map.get("foo", 3))  # Output: "bar"
print(time_map.get("foo", 4))  # Output: "bar2"
print(time_map.get("foo", 5))  # Output: "bar2"
print(time_map.get("foo", 0))  # Output: "bar3"
