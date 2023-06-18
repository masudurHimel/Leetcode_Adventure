class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mod = 10 ** 9 + 7
        @cache
        def dfs(i, j):
            res = 1
            for direction in directions:
                ni = i + direction[0]
                nj = j + direction[1]
                if 0 <= ni < m and 0 <= nj < n and grid[i][j] > grid[ni][nj]:
                    res += dfs(ni, nj) % mod 
            return res
        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod 