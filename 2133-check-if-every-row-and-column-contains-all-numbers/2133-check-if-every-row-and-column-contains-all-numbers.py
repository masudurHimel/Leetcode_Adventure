class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        res = []
        for i in matrix:
            if len(set(i)) != len(matrix):
                return False
        
        matrix[:] = zip(*matrix[::])
        
        for i in matrix:
            if len(set(i)) != len(matrix):
                return False
            
        return True
            