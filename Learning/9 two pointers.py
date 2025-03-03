'''
You are given two sorted lists A and B.
List A is partially populated with values and
has the exact number of empty slots (filled with None) to accommodate the values in list B.

Write a function that accepts two inputs, list A and list B.
The function combines the two lists, maintaining the sorting.

For example…
              i
A = [1, 2, 4, 7, None, None, None]
B = [1, 3, 9]
            j

Result: [1, 1, 2, 3, 4, 7, 9]


A = [-2, 0, 9, None, None]
B = [-101, 3]
Result: [-101, -2, 0, 3, 9]

'''
def merge_sorted_lists(A, B):
    i = len(A) - len(B) - 1  # Last filled index in A
    j = len(B) - 1           # Last index in B
    k = len(A) - 1           # Last index in A

    while j >= 0:  # Process all elements in B
        if i >= 0 and A[i] > B[j]:  # If A[i] is greater, move it to A[k]
            A[k] = A[i]
            i -= 1
        else:  # Otherwise, move B[j] to A[k]
            A[k] = B[j]
            j -= 1
        k -= 1  # Move backwards

    return A
