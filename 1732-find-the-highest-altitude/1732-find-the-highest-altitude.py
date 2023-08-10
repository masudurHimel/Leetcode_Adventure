class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = max(0, gain[0])
        for i, v in enumerate(gain[1:], 1):
            gain[i] = gain[i-1] + v
            res = max(res, gain[i])
        return res