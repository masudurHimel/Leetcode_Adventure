class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        sum = 0
        ans = 0
        for i in range(len(nums)):
            sum += nums[i]
            ans = max(ans, (sum + i) // (i + 1))
        return ans