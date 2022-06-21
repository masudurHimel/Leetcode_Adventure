class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if len(s) == 0: return True
        
        res = 0
        for i in range(len(t)):
            if s[res] == t[i]:
                res+=1
            if res >= len(s):
                break
        return res == len(s)