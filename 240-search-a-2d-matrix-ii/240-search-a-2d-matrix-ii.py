class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, 0
        
        while row < len(matrix):
            col = 0
            while col < len(matrix[0]):
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    break
                col += 1
            row += 1
        return False