class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        row, col = len(matrix) - 1, 0

        while (0 <= row < len(matrix)) and (col >= 0 and col < len(matrix[0])):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
        return False
