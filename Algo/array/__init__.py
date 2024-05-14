# https://leetcode.com/discuss/study-guide/4023666/prefix-sum-questions-to-practice

"""
Prefix sum is a powerful technique that can be used to preprocess an array to facilitate fast queries on sum of elements in particular subarrays, without modifying the original array. With the help of prefix sums, we can compute sums over subarrays in constant time.

How to Compute Prefix Sum:

Create a new array prefixSum of the same size as the original array.
prefixSum[0] = originalArray[0]
For every index i from 1 to n-1, prefixSum[i] = prefixSum[i-1] + originalArray[i]

C++ Implementation:

vector<int> computePrefixSum(vector<int>& nums) {
    int n = nums.size();
    vector<int> prefixSum(n, 0);
    prefixSum[0] = nums[0];
    for(int i=1; i<n; i++) {
        prefixSum[i] = prefixSum[i-1] + nums[i];
    }
    return prefixSum;
}

Benefits of Prefix Sum:

Quickly find the sum of any subarray using just two array lookups.
Helps in reducing the time complexity of summing over subarrays from O(n) to O(1).

Few questions to practice:
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
https://leetcode.com/problems/continuous-subarray-sum/
https://leetcode.com/problems/subarray-sum-equals-k/
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
https://leetcode.com/problems/binary-subarrays-with-sum/
https://leetcode.com/problems/path-sum-iii/
https://leetcode.com/problems/subarray-sums-divisible-by-k/
https://leetcode.com/problems/range-sum-query-2d-immutable/
https://leetcode.com/problems/count-number-of-nice-subarrays/
https://leetcode.com/problems/matrix-block-sum/
https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/
https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/
https://leetcode.com/problems/range-sum-query-immutable/
https://leetcode.com/problems/stone-game-vii/
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
https://leetcode.com/problems/defuse-the-bomb/
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
https://leetcode.com/problems/ways-to-make-a-fair-array/
https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
https://leetcode.com/problems/maximum-erasure-value/
https://leetcode.com/problems/can-make-palindrome-from-substring/
https://leetcode.com/problems/make-sum-divisible-by-p/
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/
https://leetcode.com/problems/number-of-wonderful-substrings/

"""