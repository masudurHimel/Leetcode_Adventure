class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s) <= 0:
            return True
        
        for j in t:
            if s[i] ==  j:
                i += 1
            
            if i >= len(s):
                break
        if i < len(s):
            return False
        return True