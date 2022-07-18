class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        count = 0
        temp_map = {0:1}
        temp_sum = 0
        for i in nums:
            count += temp_map.get(i-k, 0)
            
            temp_map[i] = temp_map.get(i, 0) + 1
            
        return count
                