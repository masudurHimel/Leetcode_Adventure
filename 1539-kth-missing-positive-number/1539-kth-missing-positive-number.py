class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        
        for i in range(1,len(arr)):
            if arr[i] > i+k:
                return i+k
        
        return k+len(arr)