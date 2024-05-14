from collections import defaultdict


def count_identical_twins(nums):
    count = 0
    index_map = defaultdict(int)

    for num in nums:
        if num in index_map:
            count += index_map.get(num)
        index_map[num] += 1

    return count


print(count_identical_twins([1,1,1,1]))