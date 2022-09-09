class Solution:
    def check(self, nums: List[int]) -> bool:
        num_violation = 0
        for i in range(1,len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            else:
                num_violation += 1
            
            if num_violation > 1:
                return False
        if num_violation == 1 and nums[-1] <= nums[0]:
            return True
        elif num_violation == 0:
            return True
        return False
            