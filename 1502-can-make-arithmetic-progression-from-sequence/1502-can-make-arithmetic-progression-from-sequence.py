class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]):
        if len(arr) <=2:
            return True
        
        arr.sort(reverse=True)
        res_diff = arr[0] - arr[1]
        
        for i in range(2, len(arr)):
            if arr[i-1] - arr[i] != res_diff:
                return False
        
        return True