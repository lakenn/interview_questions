"""
Given an array A[] of n integers,
the task is to find a subsequence of size k whose product is maximum among all possible k sized subsequences of the given array.

Thinking process
1) sub-sequence: doesn't need to be continuous => can sort the array
2) min can suddenly become max due to double negative
    k is
    -> odd
    -> even
3) edge case - avoid including zero ?

[-10, -8, -6, 0, 2, 6, 8, 10]

k is even:
              |
              v
[      |       ]    => A[-1], A[-2] > abs(A[0], A[1])
            * *
[      |       ]
 * *

[      |       ]
* *         * *

k is odd
[      |        ]
            ***

[      |        ]
 * *           *

can it be broken down to subproblem ?
eg,
S[1]: [    |  *]                => A[n-1]
S[2]: [    | **] or [** |  ]    => A[0]A[1] vs A[n-1]*A[n-2]
S[3]: [**  |  *] or [   | ***]  => S[1] * A[left]A[left-1] vs S[1] * A[right]A[right-1]
S[4]: [**,** | ] or [**  | **] or [   | ****]    => S[2]*A[left]A[left-1] vs S[2]*A[right]A[right-1]
S[5]: [**,** |  *] or [** | **,*] or [   | **,**,*]

"""

def sol(A, k):
    if k == 0:
        return 0

    A.sort()
    n = len(A)
    max_product = 1
    left, right = 0, n-1

    while k > 1:
        left_pair = A[left]*A[left + 1]
        right_pair = A[right]*A[right - 1]

        if left_pair > right_pair:
            max_product *= left_pair
            left += 2
        else:
            max_product *= right_pair
            right -= 2
        k -= 2

    if k > 0:
        max_product *= A[right]
    return max_product


def sol(A, k):
    if k == 0:
        return 1  # Neutral product, not 0

    A.sort()  # Sort array to access largest/smallest elements easily
    n = len(A)

    # If k = 1, just take the largest element
    if k == 1:
        return max(A)

    max_product = 1
    left, right = 0, n - 1

    # If k is odd, take the largest available element first
    if k % 2 == 1:
        max_product *= A[right]
        right -= 1
        k -= 1

    # Process elements in pairs
    while k > 0:
        left_pair = A[left] * A[left + 1]
        right_pair = A[right] * A[right - 1]

        if left_pair > right_pair:
            max_product *= left_pair
            left += 2
        else:
            max_product *= right_pair
            right -= 2

        k -= 2  # Processed 2 elements

    return max_product


print(sol([-1, -2, -4, -5, -6], 3))


# Python 3 code to find maximum possible
# product of sub-sequence of size k from
# given array of n integers

# Required function
def maxProductSubarrayOfSizeK(A, k):
    # sorting given input array
    A.sort()
    n = len(A)
    # variable to store final product of
    # all element of sub-sequence of size k
    product = 1

    # CASE I
    # If max element is 0 and
    # k is odd then max product will be 0
    if (A[n - 1] == 0 and (k & 1)):
        return 0

    # CASE II
    # If all elements are negative and
    # k is odd then max product will be
    # product of rightmost-subarray of size k
    if (A[n - 1] <= 0 and (k & 1)):
        for i in range(n - 1, n - k-1, -1):
            product *= A[i]
        return product

        # else
    # i is current left pointer index
    i = 0

    # j is current right pointer index
    j = n - 1

    # CASE III
    # if k is odd and rightmost element in
    # sorted array is positive then it
    # must come in subsequence
    # Multiplying A[j] with product and
    # correspondingly changing j
    if (k & 1):
        product *= A[j]
        j -= 1
        k -= 1

    # CASE IV
    # Now k is even. So, Now we deal with pairs
    # Each time a pair is multiplied to product
    # ie.. two elements are added to subsequence
    # each time. Effectively k becomes half
    # Hence, k >>= 1 means k /= 2
    k >>= 1

    # Now finding k corresponding pairs to get
    # maximum possible value of product
    for itr in range(k):

        # product from left pointers
        left_product = A[i] * A[i + 1]

        # product from right pointers
        right_product = A[j] * A[j - 1]

        # Taking the max product from two
        # choices. Correspondingly changing
        # the pointer's position
        if (left_product > right_product):
            product *= left_product
            i += 2

        else:
            product *= right_product
            j -= 2

    # Finally return product
    return product

print(maxProductSubarrayOfSizeK([-1, -2, -4, -5, -6, -7], 4))