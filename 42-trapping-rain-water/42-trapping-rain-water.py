class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        if len(height) <= 2:
            return 0
        
        res = 0
        lm, rm = height[0], height[len(height) - 1]
        i , j = 0, len(height) -1
        while i < j:
            lm = max(lm, height[i])
            rm = max(rm, height[j])
            if lm <= rm:
                res += lm - height[i]
                i += 1
            else:
                res += rm - height[j]
                j -= 1
        return res