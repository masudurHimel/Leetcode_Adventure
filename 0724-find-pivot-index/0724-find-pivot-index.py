class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        nums = [0] + nums + [0]
        
        for i in range(1, len(nums)-1):
            if nums[i-1] == nums[-2] - nums[i]:
                return i - 1
        return -1
            