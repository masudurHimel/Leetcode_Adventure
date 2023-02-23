from heapq import heappush, heapify, heappop
class Solution:
    def findMaximizedCapital(self, k: int, w: int, Profits: List[int], Capital: List[int]) -> int:
        heap_1 = [[-profit, capital] for profit, capital in zip(Profits, Capital)]
        heap_2 = []
        heapify(heap_1)
        
        while heap_1 and k:
            if heap_1[0][-1] <= w:
                profit, capital = heappop(heap_1)
                w += -profit
                k -= 1
            else:
                profit, capital = heappop(heap_1)
                heappush(heap_2, [capital, profit])
            while heap_2 and heap_2[0][0] <= w:
                capital, profit = heappop(heap_2)
                heappush(heap_1, [profit, capital])
        return w