class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        res = []
        for i in range(len(matrix)):
            _ = []
            for j in range(len(matrix)-1, -1, -1):
                _.append(matrix[j][i])
            res.append(_)
        matrix[:] = res
        