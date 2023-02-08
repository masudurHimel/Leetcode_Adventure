class Solution:
    def jump(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * n
        for i in range(1, n):
            dp[i] = float("inf")
            for j in range(i):
                if i <= j + nums[j] and dp[j] != float("inf"):
                    dp[i] = min(dp[i], dp[j] + 1)
                    break
        return dp[-1]
