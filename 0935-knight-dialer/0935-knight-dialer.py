class Solution:
    def knightDialer(self, n: int) -> int:
        jump = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9],
                5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]
                }

        dp = [[-1] * n for _ in range(10)]

        def backtrack(d1, nLeft):
            if nLeft == 0:
                return 1

            if dp[d1][nLeft] != -1:
                return dp[d1][nLeft]

            total_ways = 0
            for d2 in jump[d1]:
                total_ways += backtrack(d2, nLeft - 1)
            dp[d1][nLeft] = total_ways % (10**9 + 7)
            return dp[d1][nLeft]

        ans = 0
        for d in range(10):
            ans += backtrack(d, n - 1)
            ans %= 10**9 + 7

        return ans
