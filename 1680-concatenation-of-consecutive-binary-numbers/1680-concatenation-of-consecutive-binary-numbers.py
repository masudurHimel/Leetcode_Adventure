class Solution:
    def concatenatedBinary(self, n: int) -> int:
        target = ""
        for i in range(1, n+1):
            target += bin(i)[2:]
        return int(target, 2) % (10**9 + 7)