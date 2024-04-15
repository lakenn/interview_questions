import collections
import heapq

def nthUglyNumber(n):
    if n == 1:
        return 1

    ugly_numbers = {1}  # Use a set to store unique ugly numbers
    heap = [1]  # Initialize the heap with the first ugly number

    for _ in range(n - 1):
        # Pop the smallest ugly number from the heap
        current_ugly = heapq.heappop(heap)

        # Generate the next ugly numbers by multiplying the current ugly number with 2, 3, and 5
        for factor in [2, 3, 5]:
            next_ugly = current_ugly * factor
            if next_ugly not in ugly_numbers:
                ugly_numbers.add(next_ugly)
                heapq.heappush(heap, next_ugly)

    return heapq.heappop(heap)


# Example usage:
n = 10
print("The", n, "th ugly number is:", nthUglyNumber(n))

# 1,2,3,4,5,6

'''
1 * 2 = 2
1 * 3 = 3
2 * 2 = 4
1 * 5 = 5
2 * 3 = 6
3 * 2 = 6 <-- redundant

1*2, 2*2, 3*2, 4*2, ...
1*3, 2*3, 3*3, 4*3, ...
1*5, 2*5, 3*5, 4*5, ...
we take the elements in order of -
1*2, 1*3, 2*2, 1*5, 2*3, 3*3, 2*5, ...
'''

# https://www.geeksforgeeks.org/3-way-merge-sort/

def nth_ugly_number_dp(n):
    ptr2 = ptr3 = ptr5 = 0
    ugly_number = [1]

    while len(ugly_number) < n:
        next_ugly_number = min(ugly_number[ptr2]*2, ugly_number[ptr3]*3, ugly_number[ptr5]*5)
        ugly_number.append(next_ugly_number)

        if ugly_number[ptr2]*2 == next_ugly_number:
            ptr2 += 1
        if ugly_number[ptr3]*3 == next_ugly_number:
            ptr3 += 1
        if ugly_number[ptr5]*5 == next_ugly_number:
            ptr5 += 1

    return ugly_number[-1]


print(nth_ugly_number_dp(10))

# import required modules
from collections import OrderedDict

# create dictionary
od = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

# iterating over the ordereddict
for item in od.items():
    print(item)


# Decorator function
# Extra Pythonic!
class DictLikeType(collections.abc.MutableMapping):
    def __init__(self, *args, **kwargs):
        self.store = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self.store[key]
