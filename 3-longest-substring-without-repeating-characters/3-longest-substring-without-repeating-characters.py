class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        res_seen = {}
        res = 0
        
        while r < len(s):
            if s[r] in res_seen:
                l = max(l, res_seen[s[r]] + 1)
            res = max(res, r-l+1)
            res_seen[s[r]] = r
            r += 1
        
        return res