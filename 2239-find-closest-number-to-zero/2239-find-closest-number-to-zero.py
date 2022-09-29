from sortedcontainers import sortedlist
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        cp = math.inf
        cn = []
        for i in nums:
            if i >= 0:
                cp = i
                break
        
        for i in nums:
            if i < 0:
                cn.append(i)
            elif i > 0:
                break
        
        cn = cn[-1] if cn else math.inf
        
        if abs(cp) <= abs(cn):
            return cp
        else:
            return cn