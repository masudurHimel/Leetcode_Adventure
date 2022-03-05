class Solution:
    def diagonalSum(self, mat: List[List[int]]):
        i, j = 0, len(mat) - 1
        res = 0
        while i < len(mat):
            res += mat[i][i]
            if i != j:
                res += mat[i][j]
            i += 1
            j -= 1
        return res