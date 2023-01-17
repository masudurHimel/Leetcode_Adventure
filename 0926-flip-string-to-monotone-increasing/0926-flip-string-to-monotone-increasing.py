class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        flip = 0
        for i in s:
            if i == '1':
                ones += 1
            else:
                flip = min(flip+1, ones)
        return flip