class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) < 2 and len(newInterval) == 0:
            return intervals
        intervals.append(newInterval)
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        res = []

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                res.append([start, end])
                start = interval[0]
                end = interval[1]
        res.append([start, end])
        return res