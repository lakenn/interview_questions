arr = [-1, -2, -3, -2, -4, -3]
# https://www.interviewbit.com/blog/maximum-subarray-sum/
# if empty array is allowed
def largest_cont_sum(input):
    cumsum = 0
    max_value = -1e10

    for elem in input:
        cumsum += elem

        # if cumsum is smaller than zero
        if cumsum < 0:
            # meaning dun take the elem
            cumsum = 0

        if max_value < cumsum:
            max_value = cumsum

    return max_value

# when to reset current_sum ?
# iterate thru the arr, if adding arr[i] is smaller than arr[i] itself, set cur_sum = arr[i]
def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = -1e10
    current_sum = 0
    for x in numbers:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

# Subarray [5, -1, 2, -4, 6] is the max sum contiguous subarray with sum 8.
arr = [-3, -4, 5, -1, 2, -4, 6, -1]
arr = [-1]
print(max_subarray(arr))