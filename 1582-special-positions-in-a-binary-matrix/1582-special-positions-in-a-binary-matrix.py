class Solution:
    def numSpecial(self, mat: List[List[int]]):
        t_mat = list(zip(*mat))
        res = 0
        s_d = {}
        f_d = {}
        for row in range(len(mat)):
            for j in range(len(mat[0])):
                _ = s_d.get(j, sum(t_mat[j]))
                _a = f_d.get(row, sum(mat[row]))
                if mat[row][j] == 1 and _a == 1 and _ == 1:
                    res += 1
        return res
                    