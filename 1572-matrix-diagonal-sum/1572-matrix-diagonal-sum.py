class Solution:
    def diagonalSum(self, mat: List[List[int]]):
        i = 0
        res = 0
        while i < len(mat):
            res += mat[i][i]
            i += 1
        i,j = 0, len(mat) - 1
        
        while i< len(mat):
            if i!=j:
                res += mat[i][j]
            i += 1
            j -= 1
            
        return res