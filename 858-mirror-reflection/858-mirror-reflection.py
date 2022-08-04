class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        y = math.lcm(p,q) // p 
        x = math.lcm(p,q) // q
        print(x,y)
        x, y = x%2, y%2
        print(x,y)
        if x==0 and y==1:
            return 2
        elif x == 1 and y == 1:
            return 1
        elif x == 1 and  y == 0:
            return 0
        
        
        