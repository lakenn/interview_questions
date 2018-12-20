'''

Task
Given an array, find the integer that appears an odd number of times.

Example:
[5,1,1,5,2,2,5]
 ^     ^     ^
The number 5 appears 3 times, therefore the answer is 5
Specification
find_odd(integers)
Finds the number that occurs an odd amount of times

Parameters
integers: Array (of Integers) - Array with numbers to check

Return Value
Integer - The number that occurs an odd amount of times

Constraints
There will always be only one integer that appears an odd number of times

Examples
integers	Return Value
[1,1,1]	1
[4,10,4,10,6,10,6,10,6,10,6]	10


'''
def find_odd(integers):
    result = 0

    for element in integers:
        result = result ^ element

    return result