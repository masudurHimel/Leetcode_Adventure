class Solution:
    def minimumTotal(self, triangle):
        res = triangle[0][0]
        dp = [] + triangle
        for i in range(1, len(triangle)):
            for j in range(0, len(triangle[i])):
                if j == 0:
                    dp[i][j] += dp[i - 1][j]
                elif j == i:
                    dp[i][j] += dp[i - 1][j - 1]
                else:
                    dp[i][j] += min(dp[i - 1][j], dp[i - 1][j - 1])
        return min(triangle[-1])