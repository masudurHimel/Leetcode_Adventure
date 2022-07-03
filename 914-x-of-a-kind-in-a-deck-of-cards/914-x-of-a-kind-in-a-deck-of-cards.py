class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck_hash = {}
        for i in deck:
            deck_hash[i] = deck_hash.get(i, 0) + 1
        return math.gcd(*list(deck_hash.values())) >= 2