class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        if len(time) == 1:
            return totalTrips * time[0]
        l, r = 0, 10**15
        while l < r:
            mid = (l + r) // 2
            res = 0
            for t in time:
                res += mid // t
            if res >= totalTrips:
                r = mid
            else:
                l = mid + 1
        return l