class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while True:
            if i*i >c:
                break
            j = sqrt(c-(i*i))
            if j == int(j):
                return True
            i += 1
        return False