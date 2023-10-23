class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return round(log(n,4), 9) == round(log(n,4)) if n >= 1 else False