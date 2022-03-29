class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[0] != 0:
            return 0
        
        prev = nums[0]
        for i in nums[1:]:
            if i != prev + 1:
                return prev+1
            prev = i
        return prev + 1