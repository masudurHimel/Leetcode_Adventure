class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        temp_map = {0:1}
        temp_sum = 0
        for i in nums:
            temp_sum += i
            count += temp_map.get(temp_sum-k, 0)
            temp_map[temp_sum] = temp_map.get(temp_sum, 0) + 1
            
        return count
                