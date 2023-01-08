class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def get_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x1-x2 == 0:
                return math.inf
            return (y1-y2)/(x1-x2)
        
        if len(points) <= 2:
            return len(points)
        
        ans = 1
        for i in range(len(points)):
            slopes = defaultdict(int)
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                slope = get_slope(p1, p2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans+1