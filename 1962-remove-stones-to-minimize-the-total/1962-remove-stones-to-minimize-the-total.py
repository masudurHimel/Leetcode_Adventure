from sortedcontainers import SortedList
class Solution:
    def minStoneSum(self, piles, k: int):
        piles = SortedList(piles)
        while k:
            piles.add(ceil(piles.pop() / 2))
            k -= 1
        return sum(piles)