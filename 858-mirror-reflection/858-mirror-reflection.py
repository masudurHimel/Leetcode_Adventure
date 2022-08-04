class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = math.lcm(p,q)
        y, x =  (lcm // p)% 2, (lcm // q) % 2
        if x == 0:
            return 2
        elif x == 1:
            return 1 if y == 1 else 0