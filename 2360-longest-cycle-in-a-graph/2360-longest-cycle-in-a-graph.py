class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        seen = {-1}
        self.res = -1
        
        def dfs(i):
            if i in seen:
                return i, 1
            
            seen.add(i)
            cycleNode, length = dfs(edges[i])
            if i == cycleNode:
                self.res = max(self.res, length)
            
            return cycleNode, length + 1
        
        for i in range(len(edges)):
            dfs(i)
        
        return self.res