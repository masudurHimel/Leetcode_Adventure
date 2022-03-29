class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i > 0 and not res.get(i, False):
                res[i] = 1
        lim = len(res)
        for i in range(1, lim+1):
            if not res.get(i, False):
                return i
        
        return lim+1
        