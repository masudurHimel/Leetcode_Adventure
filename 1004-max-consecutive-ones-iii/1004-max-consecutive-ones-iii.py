class Solution:
    def longestOnes(self, nums, k) -> int:
        start, end = 0, 0
        flip_count = 0
        res = 0
        while end < len(nums):
            if nums[end] == 1:
                end += 1
            elif nums[end] == 0 and flip_count < k:
                end += 1
                flip_count += 1
            else:
                if nums[start] == 0:
                    flip_count -= 1
                start += 1
            res = max(res, end-start)
        return res