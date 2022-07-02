class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        
        x = 0
        y = 0
        # print(horizontalCuts, verticalCuts)
        
        for i in range(1, len(horizontalCuts)):
            x = max(x , horizontalCuts[i]-horizontalCuts[i-1])
            
        for i in range(1, len(verticalCuts)):
            y = max(y, verticalCuts[i]-verticalCuts[i-1])
        
        # print(x,y)
        return (x*y)%(pow(10,9)+7)
            
            
        