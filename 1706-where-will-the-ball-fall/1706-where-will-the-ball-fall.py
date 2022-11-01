class Solution:
    def findBall(self, grid):
        res = []

        def checkPath(i, j):
            if i == len(grid):
                return j

            if grid[i][j] == 1 and j+1 < len(grid[0]) and grid[i][j+1] == 1:
                return checkPath(i + 1, j + 1)
            elif grid[i][j] == -1 and j-1 >= 0 and grid[i][j-1] == -1:
                return checkPath(i + 1, j - 1)
            else:
                return -1

        for j in range(len(grid[0])):
            res.append(checkPath(0, j))
            
        return res