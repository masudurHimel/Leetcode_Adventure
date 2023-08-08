class Solution:
    def longestSubarray(self, nums) -> int:
        l, r = 0, 0
        flip = 0
        res = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0 and flip < 1:
                r += 1
                flip += 1
            else:
                if nums[l] == 0:
                    flip -= 1
                l += 1
            res = max(res, r-l-1)
        return res