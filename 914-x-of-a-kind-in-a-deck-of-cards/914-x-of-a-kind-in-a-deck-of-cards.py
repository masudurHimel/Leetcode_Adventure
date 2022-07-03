class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return math.gcd(*list(Counter(deck).values())) >= 2