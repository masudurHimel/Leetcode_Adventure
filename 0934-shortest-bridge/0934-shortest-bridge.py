class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            grid[x][y] = 2
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 1: dfs(nx, ny)
                    elif grid[nx][ny] == 0: 
                        q.add((nx, ny))
                        
        m, n = len(grid), len(grid[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = set()
        
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                dfs(i, j) # paint one island to 2, border 0 add to q
                break
        
        step = 0
        q = deque(q)
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1: return step + 1
                        if grid[nx][ny] == 0: 
                            grid[nx][ny] = 2 # mark visited
                            q.append((nx, ny))
            step += 1
                        
        return step