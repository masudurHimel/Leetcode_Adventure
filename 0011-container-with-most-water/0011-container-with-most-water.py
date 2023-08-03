class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        res = -math.inf
        while start < end:
            res = max(min(height[start], height[end]) * (end-start), res)
            
            if height[end] >= height[start]:
                start += 1
            else:
                end -= 1
        return res
            
            