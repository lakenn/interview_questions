import sys
from collections import Counter

#http://thisthread.blogspot.com/2015/05/codeeval-magic-numbers.html

def no_duplicate_digit(number):
    c = Counter(number)
    if any(value > 1 for value in c.values()):
        return False

    return True

def is_magic(number):
    num_length = len(number)
    visited = [False] * num_length
    pos = 0

    while (not visited[pos]):
        visited[pos] = not visited[pos]
        pos = (int(number[pos]) + pos) % num_length

    # if we end at pos 0
    return pos == 0 and all(item == True for item in visited)


for line in sys.stdin:
    lines = line.split(' ')
    A = int(lines[0])
    B = int(lines[1])

    has_magic = False

    for number in range(A, B + 1):
        if no_duplicate_digit(str(number)) and is_magic(str(number)):
            has_magic = True
            print(number)

    if not has_magic:
        print(-1, end="")
