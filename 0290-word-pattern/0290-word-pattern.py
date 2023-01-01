class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False

        a = ""
        b = ""
        j = 0
        d = dict()
        for i in pattern:
            if i in d:
                a += d[i]
            else:
                j += 1
                a += str(j)
                d[i] = str(j)

        d = dict()
        j = 0
        for i in s.split():
            if i in d:
                b += d[i]
            else:
                j += 1
                b += str(j)
                d[i] = str(j)
        
        return a == b