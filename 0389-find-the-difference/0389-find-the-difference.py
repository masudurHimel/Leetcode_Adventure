class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        for k,v in t.items():
            if s.get(k, 0) != v:
                return k
            