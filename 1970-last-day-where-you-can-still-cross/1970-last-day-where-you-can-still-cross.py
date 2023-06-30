class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        water_cells = set()
        # here we need +2 because of borders
        parent = [i for i in range(row*col+2)]
        left_most = parent[0]
        right_most = parent[-1]

        # here we need +1 because index = 0 is for the leftmost border
        def get_index(i, j):
            return i*col + j + 1
        
        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return parent[i]
        
        def union(p, q):
            p = find(p)
            q = find(q)
            if p == q: return
            parent[q] = p
        
        for day, (i, j) in enumerate(cells):
            # we are using 0-indexed array
            i -= 1
            j -= 1

            water_cells.add((i, j))

            if j == 0: union(left_most, get_index(i, j))
            if j == col-1: union(right_most, get_index(i, j))

            # looking for water cells in 8 directions
            for di, dj in [(-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1), (0, 1), (1, 0), (1, 1)]:
                new_i, new_j = i + di, j + dj
                if -1 < new_i < row and -1 < new_j < col and (new_i, new_j) in water_cells:
                    union(get_index(i, j), get_index(new_i, new_j))

            if find(left_most) == find(right_most):
                return day
