class Solution:
    def numSquares(self, n: int) -> int:
        dp = [x**2 for x in range(0, n) if x**2<=n]
        res = [n]*(n+1)
        res[0] = 0 
        for i in range(1, n+1):
            for sq in dp: 
                if i - sq < 0: 
                    break
                if 1 +  res[i-sq] <  res[i]:
                    res[i] = 1 +    res[i-sq]    
        return  res[n]