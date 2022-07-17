class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        max_res = (n * (n-1)//2)
        if k > max_res:
            return 0
        if k == 0 or k == max_res:
            return 1
        
        MOD = pow(10,9) + 7
        
        dp = [[0] * (k+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1
        
        dp[2][1] = 1
        
        for i in range(3, n+1):
            temp_max_res = min(k, (n * (n-1)//2))
            for j in range(1, temp_max_res+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                if j >= i:
                    dp[i][j] -= dp[i-1][j-i]
                dp[i][j] = (dp[i][j] + MOD) % MOD
        return dp[n][k]