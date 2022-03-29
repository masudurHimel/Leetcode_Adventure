class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = [i for i in nums if i>0]
        res = list(set(res))
        res = sorted(res)
        
        if len(res) == 0:
            return 1
        
        prev = res[0]
        if prev > 1:
            return 1
        
        for i in res[1:]:
            if i != prev + 1:
                return prev+1
            prev = i
        return prev + 1