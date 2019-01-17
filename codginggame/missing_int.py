def solution(A):
    occurrence = [False] * (len(A) + 1)
    for item in A:
        if 1 <= item <= len(A) + 1:
            occurrence[item - 1] = True
    # Find out the missing minimal positive integer.
    for index in range(len(A) + 1):
        if occurrence[index] == False:
            return index + 1

    return -1

A = [1, 3, 4, 5]
print(solution(A))


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    total = sum(A)
    min_diff = abs(total - 2* A[0])

    left_sum = 0

    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total - left_sum

        #print(left_sum, right_sum, abs(left_sum - right_sum))
        min_diff = min(abs(left_sum - right_sum), min_diff)

    return min_diff

print(solution(A))


def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]]
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp + 1
        else:
            count[A[i]] = 1
    return A[index]