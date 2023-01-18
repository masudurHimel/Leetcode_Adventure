class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        max_res = -math.inf
        res = 0
        for i in nums:
            res += i
            max_res = max(max_res, res)
            if res < 0:
                res = 0

        min_res = math.inf
        res = 0
        for i in nums:
            res = min(i, res + i)
            min_res = min(res, min_res)

        cir_max = sum(nums) - min_res
        if cir_max == 0:
            return max_res
        return max(cir_max, max_res)