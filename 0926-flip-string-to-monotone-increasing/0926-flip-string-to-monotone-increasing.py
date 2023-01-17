class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        total = 0
        flip = 0
        for i in s:
            if i == '1':
                total += 1
            else:
                flip = min(flip+1, total)
        return flip