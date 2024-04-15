class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, res, [])
        return res

    def dfs(self, nums, index, res, path):
        # if path not in res:
        res.append(path)
        print(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, res, path + [nums[i]])

sol = Solution()
print(sol.subsetsWithDup([1,2,2]))


num = 3
i=0;
S = [1,2,3]
while(num):
    if(num & 1) :
        print(S[i]);
    num >>= 1
    i += 1
