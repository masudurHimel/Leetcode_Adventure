class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.helperPow(x, -n)
        else:
            return self.helperPow(x,n)
    
    def helperPow(self, x,n):
        if n == 0:
            return 1
        _ = self.myPow(x, n//2)
        if n%2==0:
            return _ * _
        else:
            return _*_*x
        
        