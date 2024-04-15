def remove_duplicates(nums):
    if not nums:
        return 0

    # Initialize a pointer to keep track of the unique elements
    unique_ptr = 0

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous one,
        # update the unique pointer and move the current element to the
        # position pointed by the unique pointer
        if nums[i] != nums[unique_ptr]:
            unique_ptr += 1
            nums[unique_ptr] = nums[i]

    # The length of the array up to the unique pointer position + 1
    # gives the count of unique elements
    return unique_ptr + 1, nums[:unique_ptr + 1]


# Example usage:
sorted_array = [1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
unique_count, unique_array = remove_duplicates(sorted_array)
print("Unique count:", unique_count)
print("Unique array:", unique_array)