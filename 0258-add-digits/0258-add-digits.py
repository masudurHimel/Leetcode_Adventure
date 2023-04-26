class Solution:
    def addDigits(self, num: int) -> int:
        x=[int(x1) for x1 in str(num)]
        while(sum(x)>=10):
            num=sum(x)
            x=[int(x1) for x1 in str(num)]
        return sum(x)