class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        res = 0
        start, end = 0, len(nums)-1
        
        while start < end:
            s = nums[start]+nums[end]
            if s == k:
                res += 1
                start += 1
                end -= 1
            elif s > k:
                end -= 1
            else:
                start += 1
        return res
        