from collections import deque
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        k = 'a'
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    start = (i,j)
                elif grid[i][j].isalpha():
                    k = max(k, grid[i][j].lower())
        target_mask = 2**(ord(k)+1-ord('a'))-1
        visited = set()
        que = deque([(0,*start,0)])
        while que:
            d, i, j, mask = que.popleft()
            if (i,j,mask) in visited: continue
            if target_mask == mask: return d
            visited.add((i,j,mask))
            for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                if 0<=i+di<m and 0<=j+dj<n:
                    if grid[i+di][j+dj].islower():
                        que.append( (d+1,i+di,j+dj, mask | (1 << (ord(grid[i+di][j+dj])-ord('a')))) )
                    elif grid[i+di][j+dj].isupper():
                        if (mask >> (ord(grid[i+di][j+dj])-ord('A'))) & 1:
                            que.append( (d+1,i+di,j+dj,mask) )
                    elif grid[i+di][j+dj] == "." or grid[i+di][j+dj] == "@":
                        que.append( (d+1,i+di,j+dj,mask) )
        return -1