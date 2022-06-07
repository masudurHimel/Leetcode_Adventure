class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        max_res = 0
        for i in nums:
            if i-1 not in res:
                l = 1
                while i+l in res:
                    l += 1
                max_res = max(l, max_res)
        return max_res