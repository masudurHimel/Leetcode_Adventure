class Solution:
    def numSpecial(self, mat: List[List[int]]):
        t_mat = []
        res = 0
        for i in zip(*mat):
            t_mat.append(i)
            
        for row in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[row][j] == 1 and sum(mat[row]) == 1 and sum(t_mat[j]) == 1:
                    res += 1
        return res
                    