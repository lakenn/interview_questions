# https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

# Given an unsorted array A of size N that contains only non negative integers,
# find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.
#
# In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.
#
# Note:- You have to return an ArrayList consisting of two elements left and right.
# In case no such subarray exists return an array consisting of element -1.


def sub_array_sum(arr, K):
    start = 0
    currSum = 0

    # Iterate through the array using two pointers: start and end
    for end in range(len(arr)):
        currSum += arr[end]

        # shrink the window from beginning
        # until currSum is less than K
        while currSum > K and start < end-1:
            currSum -= arr[start]
            start += 1

        if currSum == K:
            return start, end

    return -1


print(sub_array_sum([1, 4, 20, 3, 10, 5], 33))
print(sub_array_sum([1, 1, 2, 3, 10, 5], 33))

