def findMaxLength(nums: list[int]) -> int:
    count = 0  # Running sum
    max_length = 0
    hash_map = {0: -1}  # To store first occurrence of a sum

    for i, num in enumerate(nums):
        count += 1 if num == 1 else -1  # Convert 0 to -1 and keep a running sum

        if count in hash_map:
            max_length = max(max_length, i - hash_map[count])
        else:
            hash_map[count] = i  # Store first occurrence of this sum

    return max_length


# Example usage:
print(findMaxLength([0, 1]))  # Output: 2
print(findMaxLength([0, 1, 0]))  # Output: 2
print(findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]))  # Output: 4

def max_len_equal_binary(nums):
    prefix_map = {}  # No {0: -1} initialization
    prefix_sum = 0
    max_length = 0

    for i, num in enumerate(nums):
        # Convert 0s to -1s
        prefix_sum += -1 if num == 0 else 1

        # If prefix sum is zero, update max_length from the beginning
        if prefix_sum == 0:
            max_length = i + 1  # The whole array from 0 to i is balanced

        # If prefix sum is seen before, update max_length
        if prefix_sum in prefix_map:
            max_length = max(max_length, i - prefix_map[prefix_sum])
        else:
            prefix_map[prefix_sum] = i  # Store first occurrence

    return max_length

# Example Usage:
nums = [0, 1, 0]
print(max_len_equal_binary(nums))  # Output: 2 ([0,1] or [1,0])
