class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]):
        res = -1
        min_dist = 99999999
        for n, i in enumerate(points):
            if i[0] == x or i[1] == y:
                _ = abs(x-i[0]) + abs(y-i[1])
                if _ < min_dist:
                    min_dist = _
                    res = n
        return res