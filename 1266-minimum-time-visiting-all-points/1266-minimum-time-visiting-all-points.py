from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(y[1] - x[1]), abs(y[0] - x[0])) for x, y in zip(points, points[1:]))
