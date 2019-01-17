#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fibonacci' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def dp_fib(n):
    fib_array = [0] * n

    if n > 1:
        fib_array[1] = 1

    if n <= 2:
        return fib_array

    for i in range(2, n):
        fib_array[i] = fib_array[i-2] + fib_array[i-1]

    return fib_array

def fibonacci(n):
    # Write your code here
    fib_array = [0, 1]

    while len(fib_array) < n + 1:
        fib_array.append(0)

    if n == 1:
        return fib_array[:n]
    else:
        for i in range(2, n):
            fib_array[i] = fib_array[i - 1] + fib_array[i - 2]

    return fib_array[:n]


if __name__ == '__main__':
    print(fibonacci(5))
    print(dp_fib(5))