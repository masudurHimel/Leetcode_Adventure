class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, i, j):
            if i < 0 or j <0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            
            grid[i][j] = '_'
            dfs(grid, i-1,j)
            dfs(grid, i+1,j)
            dfs(grid, i,j+1)
            dfs(grid, i,j-1)
            
        
        res = 0
        
        if not grid:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    res+=1
                    
        return res
    
        