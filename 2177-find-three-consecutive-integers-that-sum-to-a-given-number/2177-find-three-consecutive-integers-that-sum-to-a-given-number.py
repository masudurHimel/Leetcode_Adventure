class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # return [x-1, x, x+1] if False else x:=num//3 if num%3==0 else []
        
        # if num%3 == 0:
        #     x = num//3
        #     return [x-1, x, x+1]
        # else:
        #     return []
        
        return [x-1, x, x+1] if ((x:=num//3) and num%3==0) else [] if num!=0 else [-1,0,1]
       