class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if n == 1 and flowerbed[0] == 0:
                return True
            elif n == 0:
                return True
            else:
                return False
        for i, v in enumerate(flowerbed):
            if v == 0:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1 
                        n -= 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
            if n <= 0:
                break
        return n <= 0
            
        