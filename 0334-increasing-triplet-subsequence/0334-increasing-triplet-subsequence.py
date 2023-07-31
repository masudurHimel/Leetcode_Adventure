class Solution:
    def increasingTriplet(self, nums):
        f, s = math.inf, math.inf

        for i in nums:
            if i <= f:
                f = i
            elif i <= s:
                s = i
            else:
                return True
        return False 