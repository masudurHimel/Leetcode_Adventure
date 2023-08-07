class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                    l,r = 0,len(matrix[i])-1
                    while l<=r:
                        mid = (l+r)//2
                        print(mid)
                        if matrix[i][mid] == target:
                            return True
                        elif matrix[i][mid] < target:
                            l = mid+1
                        else:
                            r = mid-1
                            
            elif matrix[i][0] > target:
                return False
        return False