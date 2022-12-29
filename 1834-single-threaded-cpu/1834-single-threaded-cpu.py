class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        queue = []
        for i, t in enumerate(tasks):
            queue.append(t+[i])
        queue = deque(sorted(queue))

        sq = []
        order = []
        currTime = queue[0][0]
        while sq or queue:
            while (queue and queue[0][0] <= currTime) or not sq:
                enq, pt, i = queue.popleft()
                heapq.heappush(sq, [pt, i, enq])
            
            pt, i, enq = heapq.heappop(sq)
            order.append(i)
            currTime = max(currTime+pt, enq+pt)
        return order