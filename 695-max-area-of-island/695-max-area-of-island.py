class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and (i,j) not in seen:
                    stack = [(i,j)]
                    shape = 0
                    seen.add((i,j))
                    
                    while stack:
                        x, y = stack.pop()
                        shape += 1
                        targeted_list = [(x-1,y), (x+1, y), (x, y-1), (x, y+1)]
                        for x,y in targeted_list:
                            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                                if grid[x][y] and (x,y) not in seen:
                                    seen.add((x,y))
                                    stack.append((x,y))
                    res = max(res, shape)
        return res