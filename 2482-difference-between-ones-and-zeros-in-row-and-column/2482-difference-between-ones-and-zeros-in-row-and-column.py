class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row = []
        col = []
        
        for i in grid:
            row.append(
                {
                    1: i.count(1),
                    0: i.count(0)
                }
            )
        
        t_grid = zip(*grid)
        
        for i in t_grid:
            col.append(
                {
                    1: i.count(1),
                    0: i.count(0)
                }
            )
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] = row[r][1] + col[c][1] - row[r][0] - col[c][0]
        
        return grid