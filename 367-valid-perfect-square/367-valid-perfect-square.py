class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while True:
            res = i*i
            if res == num:
                return True
            elif res > num:
                return False
            i += 1
        return False