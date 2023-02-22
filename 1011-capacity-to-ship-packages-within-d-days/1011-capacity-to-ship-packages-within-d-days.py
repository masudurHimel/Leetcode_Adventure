class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = (l + r) / 2
            res, curr = 1, 0
            
            for w in weights:
                if curr + w > m:
                    res += 1
                    curr = 0
                curr += w
                
            if res > days: 
                l = m + 1
            else: 
                r = m
                
        return int(l)