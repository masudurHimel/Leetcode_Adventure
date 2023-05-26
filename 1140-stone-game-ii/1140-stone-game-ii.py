from itertools import accumulate

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        acc = list(accumulate(piles, initial = 0))
        n = len(piles)
        @cache
        def dfs(i, M):
            if i == n: return 0
            res = float('-inf')
            for j in range(i,min(i+2*M, len(piles))):
                res = max(res, acc[j+1]-acc[i]-dfs(j+1, max(M,j-i+1)))
            return res
        return (sum(piles) + dfs(0, 1))//2