class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start, end = 0, k
        prev_res = sum(nums[start:end])
        res = prev_res / k
        
        while end < len(nums):
            prev_res = (prev_res - nums[start] + nums[end])
            res = max(prev_res/k, res)
            start, end = start+1, end+1
            
        return res