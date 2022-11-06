class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            res = s
            temp = s
            for i in range(len(s)):
                temp = temp[1:] + temp[0]
                res = min(res, temp)
            return res
        return ''.join(sorted(s))