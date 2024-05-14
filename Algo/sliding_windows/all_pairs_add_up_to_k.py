# Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.
#
# Note: All pairs should be printed in increasing order of u. For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then
# (u1,v1) should be printed first else second.

# https://medium.com/enjoy-algorithm/check-for-pair-in-an-array-with-a-given-sum-c92890269a29

from collections import Counter


def find_pairs_with_sum(A, B, K):
    element_count = Counter(A)
    pairs = set()

    for num in B:
        complement = K - num
        if element_count[complement] > 0:
            pairs.add((min(num, complement), max(num, complement)))

    return pairs

A = [1, 2, 4, 5, 7]
B = [5, 6, 3, 4, 8]
K = 9

result_pairs = list(find_pairs_with_sum(A, B, K))
result_pairs.sort(key=lambda pair: pair[0])

for pair in result_pairs:
    print(pair)