class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        res = log2(n)
        if res == int(res):
            return True
        else:
            return False