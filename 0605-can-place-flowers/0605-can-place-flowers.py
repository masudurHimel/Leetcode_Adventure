class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = False
        
        if n == 0:
            return True
                
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                f = True
            elif f:
                f = False
            elif i == len(flowerbed) - 1 and flowerbed[i] != 1 and not f:
                n -= 1
                f = True
            elif flowerbed[i+1] != 1:
                n -= 1
                f = True
            
            if n == 0:
                return True

        if n:
            return False
        return True
                
            