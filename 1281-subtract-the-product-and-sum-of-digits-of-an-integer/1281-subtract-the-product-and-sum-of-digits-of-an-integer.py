class Solution:
    def subtractProductAndSum(self, n: int):
        n = list(str(n))
        res_m = 1
        res_s = 0
        for i in n:
            i = int(i)
            res_m *= i
            res_s += i
        return res_m - res_s
            
    
        
            