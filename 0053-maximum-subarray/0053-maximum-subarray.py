class Solution:
    def maxSubArray(self, nums):
        greedy = [nums[-1]] * len(nums)
        res = nums[-1]
        
        if len(nums) <= 1:
            return nums[0]
        
        for i in range(len(nums) - 2, -1, -1):
            greedy[i] = max(nums[i], greedy[i+1]+nums[i])
            res = max(res, greedy[i])
        return res