class Solution:
    def findTheDifference(self, s: str, t: str):
        s, t = list(s), list(t)
        for i in s:
            t.remove(i)
        return t[0]
            