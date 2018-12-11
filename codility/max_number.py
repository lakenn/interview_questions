def solution(A):
    N = len(A)
    result = 0
    for i in range(N):
        for j in range(N - 1, i, -1):
            # it is smaller than the best result found so far
            if j - i < result:
                break

            print(i,j)
            if A[i] != A[j]:
                result = j - i
                break

    return result

#input = [4, 6, 2, 2, 6, 6, 4]
input = [2,2,2,2,2,2,2]
print(solution(input))