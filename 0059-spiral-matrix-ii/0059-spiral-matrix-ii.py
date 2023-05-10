class Solution:
    def generateMatrix(self, n):
        max_i = n
        max_j = n
        min_i, min_j = 1, 0
        i, j = 0, 0
        res = []
        target_index = "j"
        is_j_inc = True
        is_i_inc = True
        add_token = True
        tc = n * n
        sc = 0
        target_mat = 1
        m = dict()
        while True:
            if sc == tc:
                break

            # if add_token:
            sc += 1
            res.append(target_mat)
            m[(i, j)] = target_mat

            if target_index == "j":
                if is_j_inc:
                    j += 1
                else:
                    j -= 1

                if j >= max_j:
                    j -= 1
                    target_index = "i"
                    is_j_inc = False
                    i += 1
                    max_j -= 1
                    add_token = False
                elif j < min_j:
                    j += 1
                    target_index = "i"
                    is_j_inc = True
                    i -= 1
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
                    j -= 1
                    add_token = False
                elif i < min_i:
                    i += 1
                    target_index = "j"
                    is_i_inc = True
                    min_i += 1
                    j += 1
                    add_token = False
                else:
                    add_token = True
            target_mat += 1

        r = [[0 for i in range(n)] for j in range(n)]

        for k, v in m.items():
            i, j = k
            r[i][j] = v
        return r