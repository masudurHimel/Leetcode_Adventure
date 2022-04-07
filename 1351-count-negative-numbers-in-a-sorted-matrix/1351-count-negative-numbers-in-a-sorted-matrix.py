class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res_count = 0
        for i in grid:
            for j in i[-1::-1]:
                if j >= 0:
                    break
                else:
                    res_count += 1
        return res_count
            