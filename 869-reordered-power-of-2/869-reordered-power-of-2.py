class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n = sorted(str(n))
        for i in range(30):
            i = sorted(str(2**i))
            if len(i) > len(n):
                return False
            if i == n:
                return True
        return False