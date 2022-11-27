from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n,  res = len(nums), 0
        dp = defaultdict(int)
        for j in range(n):
            for i in range(j):
                diff = nums[i] - nums[j]
                res += dp[(i, diff)]
                dp[(j, diff)] += 1 + dp[(i, diff)]
        return res