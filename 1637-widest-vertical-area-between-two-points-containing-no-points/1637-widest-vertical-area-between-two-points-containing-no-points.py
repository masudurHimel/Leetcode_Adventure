class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        result = 0
        points.sort(key=lambda x: x[0])

        for index in range(len(points) - 1):
            result = max(result, points[index + 1][0] - points[index][0])

        return result
