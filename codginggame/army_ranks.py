# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from itertools import groupby


def solution(ranks):
    # write your code in Python 3.6
    ranks.sort()
    keys = []
    counts = []

    i = 0
    result = 0

    for key, grp in groupby(ranks):
        keys.append(key)
        counts.append(len(list(grp)))

        # compare with previous group's rank
        if i > 0 and keys[i - 1] == keys[i] - 1:
            result += counts[i - 1]

        i += 1

    return result

print(solution([3, 4, 3, 0, 2, 2, 3, 0, 0] ))