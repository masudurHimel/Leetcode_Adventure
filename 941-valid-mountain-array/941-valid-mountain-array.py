class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        
        increasing, decreasing = False, False
        temp = arr[0]
        for i in arr[1:]:
            if i > temp and decreasing == False:
                increasing = True
            elif i < temp and increasing == True:
                decreasing = True
            
            else:
                return False
            
            temp = i
          
        if increasing and decreasing:
            return True
        return False
            