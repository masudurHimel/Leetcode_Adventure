class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9+7

        @cache
        def dfs(i: int) -> int:
            if i == len(s):
                return 1
            
            if i == len(s)-1 and int(s[i]) <= k and int(s[i]) >= 1:
                return 1
            
            if s[i] == '0':
                return 0

            ways = 0
            num = 0
            for l in range(i, len(s)):
                num = num*10 + int(s[l])
                if num > k:
                    break
                ways = (ways + dfs(l+1)) % MOD
            return ways % MOD

        return dfs(0)