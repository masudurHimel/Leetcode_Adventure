class Solution:
    def makeGood(self, s: str) -> str:
        res = list(s)
        i = 0
        while i < len(res)-1:
            if (ord(res[i]) - 32 == ord(res[i + 1])) or (ord(res[i]) + 32 == ord(res[i + 1])):
                res.pop(i)
                res.pop(i)
                i = 0
            else:
                i += 1
        return "".join(res)