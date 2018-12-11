def solution(A):
    N = len(A)
    result = 0
    for i in range(N):
        for j in range(i, N):
            print("{} {}".format(A[i], A[j]))
            if A[i] != A[j]:
                result = max(result, j - i)
                print(result)
    return result

input = [4, 6, 2, 2, 6, 6, 4]
print(solution(input))