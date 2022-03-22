class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        if mat == target:
            return True
        

        for p in range(3):
            for i in range(len(mat)):
                for j in range(i+1, len(mat)):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
                mat[i] = mat[i][::-1]

            if mat == target:
                return True
        
        return False