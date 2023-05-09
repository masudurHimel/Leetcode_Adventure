class Solution:
    def spiralOrder(self, matrix):
        max_i = len(matrix)
        max_j = len(matrix[0])
        min_i, min_j = 1, 0
        i, j = 0, 0
        res = []
        target_index = "j"
        is_j_inc = True
        is_i_inc = True
        add_token = True
        tc = len(matrix) * len(matrix[0])
        sc = 0
        while True:
            if sc == tc:
                break

            if add_token:
                sc += 1
                res.append(matrix[i][j])

            if target_index == "j":
                if is_j_inc:
                    j += 1
                else:
                    j -= 1

                if j >= max_j:
                    j -= 1
                    target_index = "i"
                    is_j_inc = False
                    max_j -= 1
                    add_token = False
                elif j < min_j:
                    j += 1
                    target_index = "i"
                    is_j_inc = True
                    min_j += 1
                    add_token = False
                else:
                    add_token = True
            else:
                if is_i_inc:
                    i += 1
                else:
                    i -= 1

                if i >= max_i:
                    i -= 1
                    target_index = "j"
                    is_i_inc = False
                    max_i -= 1
                    add_token = False
                elif i < min_i:
                    i += 1
                    target_index = "j"
                    is_i_inc = True
                    min_i += 1
                    add_token = False
                else:
                    add_token = True
        return res
