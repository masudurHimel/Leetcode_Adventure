class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        n = sorted(nums)
        res = []
        if n[0] + 1 < n[1]:
            res.append(n[0])
        if n[-2] + 1 < n[-1]:
            res.append(n[-1])
            
        for i in range(1, len(n)-1):
            if n[i-1] + 1 < n[i] and n[i] + 1 < n[i+1]:
                res.append(n[i])
        return res