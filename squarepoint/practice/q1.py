'''
Program:     2
Description: Lambdas defined in a loop with different values all return the same result.

Author:      Tanu Nanda Prabhu
'''

squares = []  # Creating an empty list "squares"
for x in range(5):
    squares.append(lambda n=x: n ** 2)  # Lambda function, surf about it on the internet.

print("---------------------------------------------")
print(squares[2]())
print("---------------------------------------------")


import numpy

def arrays(arr):
    arr1 = numpy.array(arr, dtype = float)
    arr2 = numpy.array(arr[::-1], dtype = float)
    return arr2

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


def own_map(func, *iterables):
    # Iterate over elements from each iterable in parallel using zip
    for args in zip(*iterables):
        yield func(*args)

A = [1,2,3,4]
squared_nums = list(own_map(lambda x, y: x*x + y, A, [1, 1, 2, 2]))


def my_func(arg1, *args, kwarg1=None, **kwargs):
    print(f'arg1: {arg1}')
    print(f'args: {args}')
    print(f'kwarg1: {kwarg1}')
    print(f'kwargs: {kwargs}')

# Calling the function with various arguments
my_func(1, 2, 3, 4, kwarg1='Hello', key1='Value1', key2='Value2')


"""
arg1 is a regular positional argument.
*args collects all additional positional arguments after arg1.
kwarg1 is a keyword argument with a default value of None.
**kwargs collects all additional keyword arguments passed to the function.
"""
"""
4. Unpacking Arguments to a Function (Passing Variable Length Arguments):
When calling a function that accepts *args or **kwargs, you can unpack lists or dictionaries to pass them as arguments.

Unpacking *args:
If you have a list of arguments and want to pass them as individual positional arguments, use the * operator to unpack them.
"""


# rewrite the map function

# When using *args: All passed positional arguments are packed into a tuple.
# The tuple will contain all the arguments passed to the function, and you can access them like any other tuple inside the function.

def own_map(func, *iterables):
    iterators = [iter(it) for it in iterables]

    # while True:
    #     try:
    #         args = [next(it) for it in iterators]
    #
    #         # apply the function
    #         yield func(*args)
    #
    #     except StopIteration:
    #         break

    # zip(*iterables) will give a tuple of corresponding elements from each iterable,
    # which is exactly what we want to pass to func

    # A = [1, 2, 3]
    # B = [4, 5, 6]
    # zip(*[A, B])  # This unpacks the iterables and is equivalent to zip(A, B)

    # When you use zip(*iterables), you
    # are unpacking the individual iterables and passing them as separate arguments to zip.
    # This results in zip grouping the corresponding elements of each iterable into tuples.

    for args in zip(*iterables): # unpack tuples into list
        yield func(*args)


A = [1, 2, 3, 4]

list(map(print, [1, 2, 3, 4], [1, 1, 2, 2]))

squared_nums = list(map(lambda x, y: x * x + y, [1, 2, 3, 4], [1, 1, 2, 2]))
print(squared_nums)

squared_nums = list(own_map(lambda x, y: x * x + y, A, [1, 1, 2, 2]))
print(squared_nums)

def my_func(*args):
    print(args)
    my_func2(*args)
def my_func2(a, b, c, d):
    print(a, b, c, d)
my_list = [1, 2, 3, 4]
my_func(*my_list)  # Unpacks the list into individual arguments

funcs = (lambda: x**2 for x in range(5))

for f in funcs:
    print(f())

funcs = [lambda x: x**2 for _ in range(5)]

for i, f in enumerate(funcs):
    print(f(i))

funcs = [lambda x=x: x**2 for x in range(5)]
[print(f()) for f in funcs]

from functools import partial

# Use partial to bind the value of x to each lambda
funcs = [partial(lambda x: x**2, x=x) for x in range(5)]

# Execute each function
[print(f()) for f in funcs]


def create_functions():
    funcs = []  # Initialize an empty list

    for x in range(5):
        # Create a lambda function that captures the value of x
        funcs.append(lambda x=x: x ** 2)  # x=x captures the value of x at the time of creation

    return funcs


# Call the function to create the list of lambdas
funcs = create_functions()

# Now, call each function in the list and print the result
for f in funcs:
    print(f())


def myFun(*arg1):
   # print(*arg1)
   print(arg1)

my_tuple = ('arg1', 'arg2')
myFun(my_tuple)
myFun(1, 2)


def myFun(arg1, arg3, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


my_dict = {'arg1':1, 'arg2': 2}
myFun(**my_dict, arg3=3)