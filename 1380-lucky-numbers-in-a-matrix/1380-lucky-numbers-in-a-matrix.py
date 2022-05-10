class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        t_matrix = zip(*matrix)
        t_matrix = list(map(list, t_matrix))
        res = []
        for i in matrix:
            temp_max = min(i)
            temp_index = i.index(temp_max)
            col_max = max(t_matrix[temp_index])
            if col_max == temp_max:
                res.append(col_max)
        return res