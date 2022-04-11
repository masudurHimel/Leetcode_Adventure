class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        target_list = []
        for i in grid:
            for j in i:
                target_list.append(j)
        if k > len(target_list):
            k = k%len(target_list)
        res = target_list[-k:] + target_list[:-k]
        res_list = []
        count = 0
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(res[count])
                count += 1
            res_list.append(temp)
        
        return res_list