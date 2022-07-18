class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                matrix[i][j] += matrix[i][j-1]
        
        count = 0
        for lb in range(len(matrix[0])):
            for ub in range(lb, len(matrix[0])):
                temp_map = {0:1}
                temp_sum = 0
                
                for i in range(len(matrix)):
                    temp_sum += matrix[i][ub]
                    if lb > 0:
                        temp_sum -= matrix[i][lb-1]
                    
                    count += temp_map.get(temp_sum-target, 0)
                    temp_map[temp_sum] = temp_map.get(temp_sum, 0) + 1
                
        
        return count