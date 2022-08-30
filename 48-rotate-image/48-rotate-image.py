class Solution:
    def rotate(self, matrix):
        t_matrix = zip(*matrix)
        for i, v in enumerate(t_matrix):
            matrix[i] = list(v)[::-1]

        return matrix