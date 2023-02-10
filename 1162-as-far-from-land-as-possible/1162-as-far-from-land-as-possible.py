class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        M, N, result = len(grid), len(grid[0]), -1
        
        valid_points = {(i, j) for i in range(M) for j in range(N)}
        
        queue = collections.deque([(i, j) for i in range(M) for j in range(N) if grid[i][j] == 1])
        
        if len(queue) == M*N or len(queue) == 0:
            return -1
        
        while queue:
			
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if (x, y) not in valid_points: 
                        continue
                    if grid[x][y] == 1: 
                        continue 
                    queue.append((x, y))
                    grid[x][y] = 1
                    
            result += 1
            
        return result