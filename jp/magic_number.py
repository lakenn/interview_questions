# http://thisthread.blogspot.com/2015/05/codeeval-magic-numbers.html

#Note that
# 1. A magic number will visit every digit exactly once and
# 2. end at the leftmost digit.
# so the last visit need to be at the leftmost digit ?
# Yes

'''
We have to detect all the numbers in a given interval that are "magic".

You could find the full description of the problem, and input your solution, on CodeEval.
The most interesting part is the description of the numbers we consider as magic:

* No digits repeat.
* Beginning with the leftmost digit, take the value of the digit and move that number of digits to the right. Repeat the process again using the value of the current digit to move right again. Wrap back to the leftmost digit as necessary. A magic number will visit every digit exactly once and end at the leftmost digit.

6231 is magic because there is no duplicate digit and:
* in position 0 there is a 6, move to position 2 -> (0 + 6) % 4 = 2
* in position 2 there is a 3, move to position 1 -> (2 + 3) % 4 = 1
* in position 1 there is a 2, move to position 3 -> (1 + 2) % 4 = 3
* in position 3 there is a 1, move to position 0 -> (3 + 1) % 4 = 0

Stripping down all the less interesting code, here is how implemented this algorithm in C++.
'''