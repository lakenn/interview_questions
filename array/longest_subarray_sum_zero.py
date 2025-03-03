def max_len_subarray_zero_sum(nums):
    prefix_map = {}  # Stores first occurrence of each prefix sum
    prefix_sum = 0
    max_length = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        # If the sum is zero, update max_length from start
        if prefix_sum == 0:
            max_length = i + 1

        # If this sum was seen before, a subarray from the first occurrence to now sums to 0
        if prefix_sum in prefix_map:
            max_length = max(max_length, i - prefix_map[prefix_sum])
        else:
            # Store the first occurrence of this prefix sum
            prefix_map[prefix_sum] = i

    return max_length

# Example usage:
nums = [14, -1, 1, -6, 1, 5, 12, 17]
print(max_len_subarray_zero_sum(nums))  # Output: 5 (Subarray: [-2, 2, -8, 1, 7])

def max_len_subarray_zero_sum(nums):
    prefix_map = {0: -1}  # Initialize with {0: -1} to handle sum=0 from start
    prefix_sum = 0
    max_length = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum in prefix_map:
            max_length = max(max_length, i - prefix_map[prefix_sum])
        else:
            prefix_map[prefix_sum] = i  # Store first occurrence

    return max_length

# Example usage:
nums = [14, -1, 1, -6, 1, 5, 12, 17]
print(max_len_subarray_zero_sum(nums))  # Output: 3 (subarray: [1, 2, -3])

