'''
Given a list of integers, implement a function that returns the average of that list.



You must print the result of your function.
You must round down the result, e.g. print "30", not "30.0".
If the list is empty, your function must raise an exception. You must then catch this exception and print exactly "List is empty".

'''

import sys

numbers = [int(l.strip()) for l in sys.stdin]


# implement your function here, use the numbers variable
# your function must return the number and you then print it

def average(lst):
    if len(lst) == 0:
        raise Exception

    return sum(lst) // len(lst)


try:
    print(average(numbers))
except Exception as e:
    print("List is empty")

