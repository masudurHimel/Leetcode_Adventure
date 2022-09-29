from sortedcontainers import sortedlist
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        cp = math.inf
        cn = math.inf
        for i in range(len(nums)):
            if nums[i] >= 0:
                cp = nums[i]
                break
            if nums[i] < 0:
                cn = nums[i]
                
        if abs(cp) <= abs(cn):
            return cp
        else:
            return cn