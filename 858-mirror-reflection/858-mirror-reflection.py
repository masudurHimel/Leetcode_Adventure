class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        y, x = (math.lcm(p,q) // p) % 2, (math.lcm(p,q) // q) % 2
        if x == 0:
            return 2
        elif x == 1:
            return 1 if y == 1 else 0