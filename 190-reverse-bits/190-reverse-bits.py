class Solution:
    def reverseBits(self, n: int):
        n = bin(n)[2:]
        n = '0' * abs(len(n)-32) + n
        return int(n[::-1], 2)