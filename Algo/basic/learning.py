import re
from _decimal import getcontext, localcontext, Context, Decimal
from functools import cache


# def collect_account_ids_from_arns(arns):
#     collected_account_ids = set()
#     for arn in arns:
#         matched = re.match(ARN_REGEX, arn)
#         if matched is not None:
#             account_id = matched.groupdict()["account_id"]
#             collected_account_ids.add(account_id)
#     return collected_account_ids
#
#



a = filter(None, [None, 1, 2, 3])
print(list(a))


# cache
@cache
def calc(arg1, arg2):
  return arg1 * arg2


print(calc(2, 3))
print(calc(2, 3))

print(getcontext().prec)

with localcontext(Context(prec=50)):
  print(Decimal(355) / Decimal(113))

# https://safjan.com/python-regex-named-groups/
import re

"""We create a re.MatchObject and store it in  
   match_object variable 
   the '()' parenthesis are used to define a  
   specific group"""

match_object = re.match(
  r'(?P<Username>\w+)@(?P<Website>\w+)\.(?P<Domain>\w+)', 'jon@geekforgeeks.org')

""" w in above pattern stands for alphabetical character 
    + is used to match a consecutive set of characters  
    satisfying a given condition 
    so w+ will match a consecutive set of alphabetical characters 
    The ?P<Username> in '()'(the round brackets) is  
    used to capture subgroups of strings satisfying  
    the above condition and the groupname is  
    specified in the ''(angle brackets)in this  
    case its Username."""

# generating a dictionary from the given emailID
details = match_object.groupdict()

# printing the dictionary
print(details)


import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.perf_counter()
        self.elapsed = self.stop - self.start

# t = Timer()
# with t:
#   result = sum(range(10_000_000))

# https://www.pythonmorsels.com/creating-a-context-manager/
with Timer() as t:
  result = sum(range(10_000_000))

t.elapsed

# monkey patch
# https://realpython.com/python-with-statement/#creating-custom-context-managers
from contextlib import contextmanager
from time import time

@contextmanager
def mock_time():
  global time
  save_time = time
  time = lambda: 42
  yield
  time = save_time

with mock_time():
  print(f'Mocked time: {time()}')

time()


import sys

# List comprehension
list_comp = [x * x for x in range(10)]

# Generator expression
gen_exp = (x * x for x in range(10))

# Get the size of each object in bytes
size_list_comp = sys.getsizeof(list_comp)
size_gen_exp = sys.getsizeof(gen_exp)

print("Size of list comprehension:", size_list_comp)
print("Size of generator expression:", size_gen_exp)
print("Difference in size:", size_list_comp - size_gen_exp)


def even_numbers(limit):
  for n in range(0, limit, 2):
    yield n


def odd_numbers(limit):
  for n in range(1, limit, 2):
    yield n


# def numbers(limit):
#   yield from even_numbers(limit)
#   yield from odd_numbers(limit)
#
#
# for num in numbers(10):
#   print(num)


def accumulator():
    total = 0
    value = None
    while True:
      value = yield total
      if value is None:
        break
      total += value

acc = accumulator()
next(acc)  # Prime the generator

print(acc.send(10))
print(acc.send(20))
print(acc.send(30))


# Let's evaluate the output of the provided code using the counter generator
def counter():
    i = 0
    while True:
        received = yield i
        if received is not None:
            i = received
        else:
            i += 1

# Creating a generator instance
gen = counter()

# Evaluating the output
output1 = next(gen)  # This should output 0
output2 = gen.send(5)  # This should output 5
output3 = next(gen)  # This should output 6
output4 = next(gen)
print(output1, output2, output3, output4)
