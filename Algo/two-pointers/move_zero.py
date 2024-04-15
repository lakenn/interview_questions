def move_zero_to_end(nums):
    # Initialize a pointer to keep track of the position to place the next non-zero element
    non_zero_ptr = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            # If the current element is non-zero, swap it with the element at nonzero_ptr
            nums[non_zero_ptr], nums[i] = nums[i], nums[non_zero_ptr]
            non_zero_ptr += 1

    # for i in range(non_zero_ptr, len(nums)):
    #     nums[i] = 0

    return nums


print(move_zero_to_end([1, 0, 2, 0, 0, 7]))