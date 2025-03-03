def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1  # Two pointers
    left_max, right_max = 0, 0  # Track max height seen from both sides
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:  # Process the smaller side first
            if height[left] >= left_max:
                left_max = height[left]  # Update left_max
            else:
                water_trapped += left_max - height[left]  # Calculate trapped water
            left += 1  # Move left pointer
        else:
            if height[right] >= right_max:
                right_max = height[right]  # Update right_max
            else:
                water_trapped += right_max - height[right]  # Calculate trapped water
            right -= 1  # Move right pointer

    return water_trapped

# Example Usage:
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))  # Output: 6

"""
Why Process the Smaller Side First?
The key reason for always processing the smaller side first in the Two-Pointer Approach for trapping rainwater is:

🔹 Water trapped at any index depends on the smaller of the max heights on both sides.

Mathematical Insight:
The water level at any position i is determined by:

water trapped
=
min
⁡
(
left_max
,
right_max
)
−
height
[
𝑖
]
water trapped=min(left_max,right_max)−height[i]
Since water depends on the smaller of left_max and right_max, we process the side with the smaller height first because it is the limiting factor.

"""