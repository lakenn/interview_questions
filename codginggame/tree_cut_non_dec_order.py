# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # single tree
    if len(A) == 1:
        return 1

    # suffix[i]: True => the seq starting at A[i] continues to be
    # non-decreasing till the end of A
    suffix = [False] * len(A)
    suffix[len(A) - 1] = True

    for i in range(len(A) - 2, -1, -1):
        suffix[i] = (A[i] <= A[i + 1] and suffix[i + 1])

    answer = 0
    for i in range(0, len(A)):
        # remove tree from middle and check if it still a non-dec list
        if i > 0 and i + 1 < len(A):
            if A[i - 1] <= A[i + 1] and suffix[i + 1]:
                answer += 1
            # we can stop as this is the only way to remove ith tree
            if A[i] < A[i - 1]:
                break
        # remove tree at head and check suffix seq
        elif i == 0:
            if suffix[i + 1]:
                answer += 1

        elif i == len(A) - 1:
            answer += 1

    return answer

#print (solution([3,4,5,4]))
#print (solution([4,5,2,3,4]))
#print (solution([1,5,8,11,19]))
print(solution([4, 5, 2, 5, 5]))