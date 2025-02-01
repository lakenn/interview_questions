# https://workat.tech/problem-solving/approach/nre/non-repeating-element
"""
This observation can be used to find the answer efficiently using binary search.

Declare three variable low=0, high = n-1 and mid;
While (low<=high) assign mid=(high+low)/2.
If mid is even then check if arr[mid] and arr[mid+1] are equal. If yes, then the element must be in the second half otherwise the element must be in the first half.
If mid is odd then check if arr[mid] and arr[mid-1] are equal. If yes, then the element must be in the second half otherwise the element must be in the first half.
When low and high are equal, return the value of arr[low] as it is the only element that is not equal to its previous or next element.

"""
"""
Given a sorted list of numbers in which all elements appear twice except one element that appears only once, find the number that appears only once.
"""
arr = [1, 1, 2, 2, 3, 4, 4]

def find_non_repeating_element(arr):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right)//2

        if left == right:
            return arr[mid]

        if mid % 2 == 0:
            if arr[mid] == arr[mid+1]:
                left = mid + 1
            else:
                right = mid -1
        else:
            if arr[mid] == arr[mid-1]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

print(find_non_repeating_element(arr))