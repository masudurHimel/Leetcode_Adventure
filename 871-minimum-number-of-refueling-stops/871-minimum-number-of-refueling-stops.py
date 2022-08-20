class Solution:
    @staticmethod
    def minRefuelStops(target, startFuel, stations):
        dp = [0] * (len(stations) + 1)
        dp[0] = startFuel
        for i, v in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= v[0]:
                    dp[j + 1] = max(dp[j + 1], dp[j] + v[1])

        for i in range(len(dp)):
            if dp[i] >= target:
                return i
        return -1