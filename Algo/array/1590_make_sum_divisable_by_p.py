def minSubarray(nums, p):
    target_remainder = sum(nums) % p
    if target_remainder == 0:
        return 0

    prefix_sum = 0
    remainder_map = {0: -1}
    min_length = float('inf')

    for i, num in enumerate(nums):
        prefix_sum = (prefix_sum + num) % p
        complement = (prefix_sum - target_remainder) % p

        if complement in remainder_map:
            min_length = min(min_length, i - remainder_map[complement])

        remainder_map[prefix_sum] = i

    return min_length if min_length < len(nums) else -1


# Example usage:
nums = [6, 5, 2, 3]
p = 9
print(minSubarray(nums, p))  # Output: 4
