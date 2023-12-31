class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = defaultdict(list)
        
        for i in range(len(s)):
            d[s[i]].append(i)
        
        res = -1
        for k, v in d.items():
            if len(v) >= 2:
                res = max(res, abs(v[0]-v[-1])-1)
      
        return res