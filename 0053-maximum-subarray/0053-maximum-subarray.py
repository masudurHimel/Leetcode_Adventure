class Solution:
    def maxSubArray(self, nums):
        greedy = [nums[-1]] * len(nums)
        
        for i in range(len(nums) - 2, -1, -1):
            greedy[i] = max(nums[i], greedy[i+1]+nums[i])
        return max(greedy)