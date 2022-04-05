class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        l_i = n
        for i in range(1, l_i+1):
            if i <= n:
                res += 1
                n -= i
            else:
                break
        return res