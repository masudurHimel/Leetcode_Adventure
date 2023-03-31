class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        #pre-compute a matrix of suffixes counts
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j] = (pizza[i][j] == 'A') + dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1]

        @lru_cache(None)
        def dfs(i, j, kk):
            if dp[i][j] < kk: return 0
            if kk == 1: return 1
            #cut horizontally first then vertically
            return sum(dfs(i_, j, kk - 1) for i_ in range(i + 1, m) if dp[i][j] > dp[i_][j]) + \
            sum(dfs(i, j_, kk - 1) for j_ in range(j + 1, n) if dp[i][j] > dp[i][j_])
        
        return dfs(0, 0, k) % mod