class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x = sum(j>0 for i in grid for j in i)
        y = sum(max(i) for i in grid)
        z = sum(max(s[i] for s in grid) for i in range(len(grid)))
        
        return (x+y+z)
        
        
        