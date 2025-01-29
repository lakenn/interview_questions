import numpy as np

# Example 1: Creating a NumPy Array
# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr)


for i, point in enumerate(arr):
    print(i, point)

# Create a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", matrix)

for i, point in enumerate(matrix):
    print(i, point)

# Example 2: Array Operations
# Element-wise operations
arr = np.array([1, 2, 3, 4, 5])
print("Add 10:", arr + 10)
print("Square:", arr ** 2)

# Matrix multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
result = np.dot(matrix_a, matrix_b)
print("Matrix Multiplication:\n", result)

# Example 3: Indexing and Slicing
# Indexing
arr = np.array([10, 20, 30, 40, 50])
print("Element at index 2:", arr[2])

# Slicing
print("First three elements:", arr[:3])

# 2D Array Slicing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("First row:", matrix[0])
print("Element at (2, 2):", matrix[2, 2])  # Row 2, Column 2

# Example 4: Array Properties
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape:", arr.shape)  # (2, 3)
print("Size:", arr.size)    # 6 (total elements)
print("Data type:", arr.dtype)  # int64

# Example 5: Creating Special Arrays
# Array of zeros
zeros = np.zeros((2, 3))
print("Zeros:\n", zeros)

# Array of ones
ones = np.ones((3, 3))
print("Ones:\n", ones)

# Identity matrix
identity = np.eye(3)
print("Identity Matrix:\n", identity)

# Random array
random = np.random.rand(2, 3)
print("Random Array:\n", random)


min()