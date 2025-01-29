def generate_permutations(nums):
    # List to store the generated permutations
    generated_permutations = []

    # Helper function to perform recursion
    def permutation(current_permutation, elements_to_permute):
        # Base Case: If no elements left to permute, add the current permutation to the result
        if not elements_to_permute:
            generated_permutations.append(current_permutation)
        else:
            # Recur for each element in the remaining list of elements
            for i in range(len(elements_to_permute)):
                # Choose the current element and form the next permutation
                next_permutation = current_permutation + [elements_to_permute[i]]
                remaining_elements = elements_to_permute[:i] + elements_to_permute[i + 1:]
                # Recur with the new permutation and the remaining elements
                permutation(next_permutation, remaining_elements)

    # Initial call to the helper function with an empty permutation and the full list of elements
    permutation([], nums)

    return generated_permutations


# Example usage
nums = [1, 2, 3]
print(generate_permutations(nums))
