class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        cost = lambda i,j: abs(locations[i]-locations[j])
        @lru_cache(None)
        def dfs(i, f):
            if f<0: return 0 
            return sum([dfs(j,f-cost(i,j)) for j in range(len(locations)) if j != i]) + (i==finish)
        return dfs(start, fuel) % (10**9+7)