class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue   
                res = max(res, (nums[i]-1)*(nums[j]-1))
        return res