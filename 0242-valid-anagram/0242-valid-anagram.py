class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        t = Counter(t)
        
        if len(s) != len(t):
            return False
        
        for i in s.keys():
            if s[i] != t.get(i, 0):
                return False
        return True