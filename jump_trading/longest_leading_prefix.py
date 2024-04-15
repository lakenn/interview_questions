# Consider X=7 and Y=42. In this case, the longest prefix of array A=[6, 42, 11, 7, 1, 42] would be 4. This is because the subarray A[0]-A[4] contains an equal number of X and Y.
#
# For instance, let X be 6 and Y be 13. If A is equal to [13, 13, 1, 6], the output of the function should be -1 as there is no prefix present.
#
# The input consisting of X=100, Y=63, and A=[100,63,1,6,2,13] must result in an output of 5.

def solution(X, Y, A):
    N = len(A)
    result = -1
    nX = 0
    nY = 0
    for i in range(N):
        if A[i] == X:
            nX += 1
        elif A[i] == Y:
            nY += 1
        if nX == nY:
            result = i
    return result