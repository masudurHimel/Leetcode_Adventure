class Solution:
    def rob(self, nums):
        if len(nums) <= 1:
            return nums[0]
        res = [0] * len(nums)
        res[0], res[1] = nums[0], nums[1]

        for i in enumerate(nums[2:]):
            max_val = max(res[: 2 + i[0] - 1])
            res[2 + i[0]] = max_val + i[1]
        return max(res)