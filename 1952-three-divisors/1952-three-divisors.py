class Solution:
    def isThree(self, n: int) -> bool:
        res = [1, n]
        for i in range(2,n//2+1):
            if n % i == 0:
                res.append(i)
        return len(res) == 3