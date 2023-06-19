class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for i, v in enumerate(gain):
            res.append(res[-1]+v)
        return max(res)