class Solution:
    def longestSubarray(self, nums) -> int:
        l, r = 0, 0
        flip = 0
        res = 0
        for i, v in enumerate(nums):
            if v == 0:
                flip += 1
                if flip == 2:
                    flip = 1
                    l = r+1
                r = i
            res = max(res, i-l+1)
        return res - 1