class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m=len(cuts)

        @cache
        def dfs(l,r):

            best = 10**20
            cancut=False
            for i in cuts:
                if l<i<r:
                    best=min(best,r-l+dfs(l,i)+dfs(i,r))
                    cancut=True
            if not cancut:
                return 0
            return best

        return dfs(0,n)