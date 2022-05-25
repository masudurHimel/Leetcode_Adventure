class Solution:
    def numSpecial(self, mat: List[List[int]]):
        t_mat = list(zip(*mat))
        res = 0
        s_d = {}
        for row in range(len(mat)):
            for j in range(len(mat[0])):
                _ = s_d.get(j, sum(t_mat[j]))
                if mat[row][j] == 1 and sum(mat[row]) == 1 and _ == 1:
                    res += 1
        return res
                    