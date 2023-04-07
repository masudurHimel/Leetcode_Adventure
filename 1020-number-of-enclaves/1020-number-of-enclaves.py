class Solution:
    def numEnclaves(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i,j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                dfs(i + 1,j)
                dfs(i,j - 1)
                dfs(i,j + 1)
                dfs(i - 1,j)


        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1 and grid[i][j] == 1:
                    dfs(i,j)
        return sum(sum(row) for row in grid)