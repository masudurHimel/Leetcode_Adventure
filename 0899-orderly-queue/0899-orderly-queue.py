class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            temp = s
            for i in range(len(s)):
                temp = temp[1:] + temp[0]
                s = min(s, temp)
            return s
        return ''.join(sorted(s))