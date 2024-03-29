class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res, lis = [], []
        for i, o in enumerate(obstacles):
            idx = bisect.bisect(lis, o)
            if idx == len(lis):
                lis.append(o)
            else:
                lis[idx] = o
            res.append(idx + 1)
            
        return res