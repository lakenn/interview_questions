import random
import time
from collections import Counter, OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed

import threading

# threads = []
# for i in range(10):
#     t = threading.Thread(target=say_hello, args=(i,))
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()

import time
import random
from concurrent.futures import ThreadPoolExecutor

def say_hello(x):
    # sleep_time = random.uniform(0.5, 2)  # Random sleep between 0.5s to 2s
    # time.sleep(sleep_time)
    print(f"Hello {x}")
    return x


with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(say_hello, x) for x in range(10)]

    for future in as_completed(futures):
        print("Completed:", future.result())  # Prints results in completion order

with ThreadPoolExecutor(max_workers=5) as executor:
    result = executor.map(say_hello, [1, 2])  # Blocks until all tasks are done

print("Results:", list(result))  # Output is always in order [0, 1, 2, ... 9]

# class MyClass:
#     def __new__(cls, *args, **kwargs):
#         print(f'Creating instance of {cls.__name__}')
#         # Create a new instance of the class
#         instance = super(MyClass, cls).__new__(cls)
#         return instance
#
#     def __init__(self, value):
#         self.value = value
#
# # Creating an instance
# obj = MyClass(10)  # Output: Creating instance of MyClass
# print(obj.value)  # Output: 10


arr = list(range(8))

print(arr[::-1])
step = 3
gen = (arr[i:i+step] for i in range(0, len(arr), step))
print(next(gen))
print(next(gen))
print(next(gen))


from itertools import islice

def chunk_list(iterable, size):
    iterator = iter(iterable)  # Convert iterable to an iterator
    return iter(lambda: list(islice(iterator, size)), [])  # Closure captures `iterator`


print(list(chunk_list(arr, 3),))


print(list(islice([1,2,3,4,5], 2, 4)))

def split_into_chunks(lst, n):
    size = len(lst) // n  # Must be perfectly divisible
    it = iter(lst)
    return [list(islice(it, size)) for _ in range(n)]

print(split_into_chunks([1,2,3, 4, 5], 2))


# Find the first non-repeating character in a string.
"""
Input: s = “geeksforgeeks”
Output: ‘f’
Explanation: ‘f’ is the first character in the string which does not repeat.
"""
def non_repeating_char(s):
    c = Counter(s)
    for char in s:
        if c[char] ==  1:
            return char
    return None

print(non_repeating_char("geeksforgeeks"))

def non_repeating_char_order_dict(s):
    c = OrderedDict()
    for char in s:
        c[char] = c.get(char, 0) + 1

    for char, freq in c.values():
        if freq == 1:
            return char

    return None

def reverse_string(s):
    length = len(s)
    result = [None] * length
    for i in range(length):
        result[i] = s[length-i-1]

    return ''.join(result)

print(reverse_string('abc'))

def reverse_str_swap(s):
    left, right = 0, len(s)-1

    s = list(s)

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right += 1

    return ''.join(s)


def check_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

# Find the longest substring without repeating characters.
def longest_substr_without_repeating(s):
    left = 0
    char_set = set()
    result = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        result = max(result, right - left + 1)

    return result

print(longest_substr_without_repeating('abcdefd'))

# Find a subarray with the maximum sum
# Kadane’s Algorithm requires tracking both the current sum and the maximum sum encountered.
def max_subarr_sum(arr):
    if not arr:
        return 0

    cumsum = maxsum = arr[0]

    for num in arr[1:]:
        cumsum = max(cumsum+num, num)
        maxsum = max(cumsum, maxsum)


print(max_subarr_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


# Find pairs in an array that sum to a given value.
def sum_to_target(arr, target):
    arr.sort()

    left, right = 0, len(arr)-1

    while left < right:
        if arr[left] + arr[right] == target:
            return arr[left], arr[right]
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1

    return None

print(sum_to_target([1,2,3,4,5,6], 8))

# Reverse a linked list (iterative & recursive).
# Python program to reverse linked list using Stack

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

    def __repr__(self):
        return str(self.data)

# A -> B -> C
# C -> B -> A
def reverse_link_list(head):
    stack = []

    while head:
        stack.append(head)
        head = head.next

    dummy = node = Node(-1)

    while stack:
        node.next = stack.pop()
        node = node.next

    node.next = None

    return dummy.next

def reverse_link_list_while(head):
    prev = None
    curr = head

    while curr:
        # save the next node so you don't track
        next = curr.next

        # flip the ptr
        curr.next = prev

        # move fwd
        curr, prev = next, curr

    return prev


# Create a hard-coded linked list:
# 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def printList(node):
    while node is not None:
        print(f" {node.data}", end="")
        node = node.next
    print()

printList(reverse_link_list(head))

# Find the missing number in an array of size n with numbers 1 to n.
def find_missing(arr):
    n = len(arr) + 1
    expected_sum = (1+n)*n//2
    return expected_sum - sum(arr)


# Implement a stack with push(), pop(), and getMin().
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        # always make sure top of stack contains the min val
        min_val = val if not self.stack else min(self.stack[-1][1], val)
        self.stack.append((val, min_val))

    def pop(self):
        if self.stack:
            val, _ = self.stack.pop()
            return val
        return None

    def getMin(self):
        return self.stack[-1][1]


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)

        return cls._instance

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self, db_name):
        self.db_name = db_name

# Write a decorator that caches function results (memoization).
def memorize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)

        return cache[args]

    return wrapper


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root, target):

    if root is None:
        return None

    if root.val == target:
        return root
    elif root.val > target:
        return searchBST(root.left, target)
    else:
        return searchBST(root.right, target)

def searchBST(root, target):

    while root:
        if root.val == target:
            return root
        elif root.val > target:
            root = root.left
        else:
            root = root.right

    return None


# https://stackoverflow.com/questions/29139350/difference-between-ziplist-and-ziplist
def add(x, y):
   return x + y

t = [1,2]
print(add(*t))

# def custom_map(fn, *iterables):
#     for args in *zip(*iterables):
#         yield fn(args)
#
#
# gen = custom_map(lambda x, y: print(x+y), [1], [2])
# next(gen)
def my_map(func, iterable):
    for item in iterable:
        yield func(item)  # Apply function and yield result

# Example usage
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = my_map(square, numbers)

print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

def my_map(func, *iterables):
    for args in zip(*iterables):  # Pair elements from all iterables
        yield func(*args)  # Unpack and apply function

# Example usage
def square(x, y):
    return x * y

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]

result = my_map(square, numbers1, numbers2)

print(list(result))  # Output: [10, 40, 90, 160, 250]

# The zip() function in Python takes multiple iterables (lists, tuples, sets, strings, generators, etc.) and
# returns an iterator of tuples, where each tuple contains elements from the input iterables at the same index.

print(list(zip([1,2,3], [4,5,6])))
print(list(zip(*([1,2,3], [4,5,6]))))
print(list(zip((1,2,3), (4,5,6))))

# *args example
def fun(*args):
    return sum(args)

print(fun(1, 2, 3, 4))
print(fun(5, 10, 15))

# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)

def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1

it = counter(10)
print(next(it))
print(next(it))
print(it.send(8))


def custom_filter(func, iterable):
    for item in iterable:
        if func(item):
            yield item


print(list(custom_filter(lambda x: x > 10 and x < 20, [5, 12, 17, 20, 25])))


# Function that takes two arguments
def add(x, y):
    return x + y

# Two lists to apply the function on
list1 = [1, 2, 3]
list2 = [4, 5, 6]

def custom_map(func, *iterables):
    # iterables is a tuple
    # we need to pair item with same index from each iterable using zip
    print(*iterables, sep=", ")
    for args in zip(*iterables):
        yield func(*args)

print(list(custom_map(add, list1, list2)))

from functools import wraps, partial


def custom_partial(*partial_args, **partial_kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            prefill_args = partial_args + args
            prefill_kwargs = {**partial_kwargs, **kwargs}

            return func(*prefill_args, **prefill_kwargs)

        return wrapper

    return decorator


@custom_partial(x=2)  # Pre-filling x = 2
def multiply(x, y):
    return x * y

print(multiply(y=5))  # Output: 10 (2 * 5)
print(multiply(y=10)) # Output: 20 (2 * 10)

@custom_partial(2)  # Pre-filling x = 2
def multiply(x, y):
    return x * y

print(multiply(y=5))  # Output: 10 (2 * 5)
print(multiply(10)) # Output: 20 (2 * 10)



def custom_reduce(function, iterable, initializer=None):
    it = iter(iterable)

    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no initial value")

    result = initializer
    for element in it:
        result = function(result, element)

    return result


def print_hello(*args):
    print(args, sep=', ')
    print(*args, sep=',, ')

args = [4, 5, 6]
print_hello(1,2,3, *args)
print_hello(*args)


def multiply(x, y):
    return x * y

# Creating a partial function with a fixed keyword argument
# Setting `y` to 3, leaving `x` to be specified later
multiply_by_3 = partial(multiply, y=3)

# Now you can call `multiply_by_3` with the required argument `x`
result = multiply_by_3(5)  # Here, x is provided as 5
print(result)  # Output: 15

multiply_by_3 = partial(multiply, 3)
result = multiply_by_3(5)  # Here, x is provided as 5
print(result)  # Output: 15

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

# Usage
counter1 = make_counter()
print(counter1())  # Output: 1
print(counter1())  # Output: 2


# Create a lambda function that takes a list of integers and returns a list of squares of the even numbers only.
a = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(a)


# Write a generator function that yields the Fibonacci sequence up to n.
def fib_gen(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


def multipliers():
    return [lambda x: i * x for i in range(4)]


def multipliers():
    return [lambda x : i * x for i in range(4)]

print([m(2) for m in multipliers()])

def multipliers():
    result = []
    for i in range(4):
        result.append(lambda x, i=i: i * x)
    return result

# https://www.toptal.com/python/interview-questions
def main():
    multipliers_list = multipliers()
    results = []
    for m in multipliers_list:
        results.append(m(2))
    print(results)

if __name__ == "__main__":
    main()


def multipliers():
    for i in range(4):
        yield lambda x: i * x

print([m(2) for m in multipliers()])  # Output: [6, 6, 6, 6]


class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print("Before any changes:")
print("Parent.__dict__:", Parent.__dict__)
print("Child1.__dict__:", Child1.__dict__)
print("Child2.__dict__:", Child2.__dict__)

Child1.x = 2
print("\nAfter changing Child1.x:")
print("Parent.__dict__:", Parent.__dict__)
print("Child1.__dict__:", Child1.__dict__)
print("Child2.__dict__:", Child2.__dict__)

Parent.x = 3
print("\nAfter changing Parent.x:")
print("Parent.__dict__:", Parent.__dict__)
print("Child1.__dict__:", Child1.__dict__)
print("Child2.__dict__:", Child2.__dict__)
