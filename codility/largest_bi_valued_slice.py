def solution(A):
    if len(A) == 0:
        return 0

    last_repeat_count = 1
    bi_values = set([A[0]])
    curr_count = 1
    max_count = 1

    for i in range(1, len(A)):
        bi_values.add(A[i])
        if len(bi_values) > 2:
            # update bi_values
            bi_values = set([A[i-1], A[i]])
            curr_count = last_repeat_count + 1
            last_repeat_count = 1
        else:
            curr_count += 1

            if A[i] == A[i-1]:
                last_repeat_count += 1
            else:
                last_repeat_count = 1

        if curr_count > max_count:
            max_count = curr_count

    return max_count

print(solution([5, 4, 4, 4, 5, 5, 5, 3, 3]))
