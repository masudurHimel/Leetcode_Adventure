class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr = sorted(arr)
        dp = [1] * n
        mod = 10 ** 9 + 7
        
        ind_map = {i:x for x,i in enumerate(arr)}
        
        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    r = arr[i] / arr[j]
                    if r in ind_map:
                        dp[i] += dp[ind_map[r]] * dp[j]
                        dp[i] %= mod
        return sum(dp) % mod