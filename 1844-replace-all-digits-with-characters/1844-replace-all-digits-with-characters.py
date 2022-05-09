class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        for ind, val in enumerate(s):
            if ind%2 != 0:
                _ = s[ind-1]
                val = chr(ord(_)+int(val))
            res += val
        return res