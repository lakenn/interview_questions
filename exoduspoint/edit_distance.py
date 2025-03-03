"""
Given two strings, str1 and str2, compute the edit distance between them.

Input: Two strings str1 and str2.
Output: An integer that represents the minimum number of operations needed to convert str1 into str2.
"""
def setup():
    print(distance("kitten", "sitting"))


def distance(a, b):
    costs = []
    for j in range(len(b) + 1):
        costs.append(j)
    for i in range(1, len(a) + 1):
        costs[0] = i
        nw = i - 1
        for j in range(1, len(b) + 1):
            cj = min(1 + min(costs[j], costs[j - 1]),
                     nw if a[i - 1] == b[j - 1] else nw + 1)
            nw = costs[j]
            costs[j] = cj

    return costs[len(b)]


setup()