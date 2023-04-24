from sortedcontainers import SortedList

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = SortedList(stones)
        while len(stones):
            x = stones.pop()
            if not stones:
                return x
            y = stones.pop()
            if x == y:
                continue
            else:
                y = abs(y-x)
                stones.add(y)
        return 0