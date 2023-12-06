class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        i = 0
        for i in range(1,n//7+1):
            z = (7/2)*((2*i)+6*1)
            res += z
            
        return int(res+((n%7)/2)*((2*(i+1))+((n%7)-1)*1))