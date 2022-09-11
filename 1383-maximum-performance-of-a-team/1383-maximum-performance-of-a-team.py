class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        p = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        min_heap = []
        res = 0
        ts = 0
        for i, (s,e) in enumerate(p):
            if i < k:
                ts += s
                heapq.heappush(min_heap, s)
            elif s > min_heap[0]:
                ts += s - heapq.heappushpop(min_heap, s)
            else:
                continue
                
            res = max(res, ts * e)
        return res % (10**9+7)
            