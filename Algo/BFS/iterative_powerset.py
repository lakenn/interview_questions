def subsets(nums):
    result = [[]]  # Start with the empty subset

    for num in nums:
        # Add current number to all existing subsets
        result += [curr + [num] for curr in result]
        print(result)

    return result


# Example usage
nums = [1, 2, 3]
print(subsets(nums))
