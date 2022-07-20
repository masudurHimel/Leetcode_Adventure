class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = Counter(s)
        t = Counter(t)
        if len(s) != len(t):
            return False
        
        for i in s.keys():
            if t.get(i,0) != s[i]:
                return False
        return True