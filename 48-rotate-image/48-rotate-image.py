class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i, v in enumerate(zip(*matrix)):
            matrix[i] = list(v)[::-1]