class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []

        for i in range(n-1, -1, -1):
            while heap and heap[0][1] > i + k:
                heapq.heappop(heap)
            temp = heap[0][0] if heap else 0
            max_including = - nums[i] + temp
            heapq.heappush(heap, (max_including, i))
            
            if i == 0: 
                return -1 * max_including