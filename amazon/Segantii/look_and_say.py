'''

Your task is to create a function that will take an integer and return the result of the look-and-say function on that integer.
This should be a general function that takes as input any positive integer, and returns an integer; inputs are not limited to the sequence which starts with "1".

Conway's Look-and-say sequence goes like this:

Start with a number.
Look at the number, and group consecutive digits together.
For each digit group, say the number of digits, then the digit itself.
Sample inputs and outputs:

1 is read as "one 1" => 11
11 is read as "two 1s" => 21
21 is read as "one 2, then one 1" => 1211
9000 is read as "one 9, then 3 0s" => 1930
222222222222 is read as "twelve 2s" => 122

'''
from itertools import groupby


def look_say(number):
  number_str = str(number)
  result = ''.join(str(len(list(g))) + k for k, g in groupby(number_str))
  return int(result)

print(look_say(12))