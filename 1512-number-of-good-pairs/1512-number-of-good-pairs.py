class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i,v in enumerate(nums):
            for j, k in enumerate(nums[i+1:]):
                if v == k:
                    res += 1
        return res