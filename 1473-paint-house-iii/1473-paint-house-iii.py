class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def helper(i, prev_color, neighbor):
            if (neighbor > target) or (i==m and neighbor!=target):
                return inf
            if i==m:
                return 0
            
            if houses[i] != 0:
                return helper(i+1, houses[i], neighbor + int(prev_color!=houses[i]))
            
            best = inf
            for value, b_cost in enumerate(cost[i], 1):
                best = min(best, helper(i+1, value, neighbor + int(prev_color!=value)) + b_cost)
            
            return best
        
        res = helper(0,0,0)
        return res if res!=inf else -1