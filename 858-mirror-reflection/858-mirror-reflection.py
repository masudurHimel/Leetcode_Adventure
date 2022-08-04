class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        y = math.lcm(p,q) // p 
        x = math.lcm(p,q) // q
        x, y = x%2, y%2

        if x == 0:
            return 2
        elif x == 1:
            return 1 if y == 1 else 0
        
        
        