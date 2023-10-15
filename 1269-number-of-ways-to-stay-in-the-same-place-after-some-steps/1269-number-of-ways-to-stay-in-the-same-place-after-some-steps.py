class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [0] + [0] * min(steps, arrLen) + [0]
        dp[1] = 1

        for _ in range(steps):
            newDP = [0] + [0] * min(steps, arrLen) + [0]
            for i in range(1, len(dp)-1):
                newDP[i] = (dp[i-1] + dp[i] + dp[i+1]) % (10**9 + 7)
            dp = newDP[:]

        return dp[1]