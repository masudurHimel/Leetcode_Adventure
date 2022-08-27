import sortedcontainers
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def updateRes(nums, k):
            nonlocal res
            
            s = 0
            sortedSum = sortedcontainers.SortedSet()
            sortedSum.add(0)
            
            for num in nums:
                s += num
                x = sortedSum.bisect_left(s-k)
                if x < len(sortedSum):
                    res = max(res, s - sortedSum[x])
                    
                sortedSum.add(s)
            
        
        res = -math.inf
        
        for i in range(len(matrix)):
            row_sum = [0] * len(matrix[0])
            
            for row in range(i, len(matrix)):
                for col in range(len(matrix[row])):
                    row_sum[col] += matrix[row][col]
                    
                updateRes(row_sum, k)
                if res == k:
                    return res
            
        return res if res != -math.inf else -1 