class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])

        for r in range(1, row):
            for c in range(col):
                matrix[r][c] += matrix[r-1][c] if matrix[r][c] else 0

        ans = 0

        for r in range(row):
            matrix[r].sort(reverse=True)
            ans = max(ans, max((c + 1) * matrix[r][c] for c in range(col)))

        return ans