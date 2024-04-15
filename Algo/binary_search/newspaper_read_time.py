from typing import List

newspaper_read_time = [7, 2, 5, 10, 8]
# newspapers_read_times = [7,2,5,10,8], num_coworkers = 2

# what is infesible solution?
# num_worker needed > num_coworkers in order to achieve possible_max_time
# - subsection of consecutive newspapers <= possible_max_time

def is_fesible(arr: List[int], possible_max_time, num_coworkers):
    curr_max = 0
    required_worker = 1

    for read_time in arr:
        if curr_max + read_time <= possible_max_time:
            curr_max += read_time
        else:
            required_worker += 1
            curr_max = read_time
            if required_worker > num_coworkers:
                return False

    return True


def min_newspaper_read_time(arr: List[int], num_coworkers: int):
    left, right = max(arr), sum(arr)
    min_time = right

    # binary search the minimum newspaper reading time
    while left <= right:
        mid = (left + right)//2

        # check if mid is a fesible time given the constraint
        if is_fesible(arr, mid, num_coworkers):
            # keep looking for smaller min time
            min_time = mid
            right = mid - 1
        else:
            left = mid + 1

    return min_time

newspaper_read_time = [2,3,5,7]
print(min_newspaper_read_time(newspaper_read_time, 3))