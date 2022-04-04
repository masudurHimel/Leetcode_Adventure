class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and target == nums[0]:
            return [0,0]
        start, end = -1, -1
        flag = 0
        for i in range(len(nums)):
            if flag == 0 and nums[i] == target:
                start = i
                flag = 1
            if flag == 1 and nums[i] != target:
                end = i-1
                flag = 0
                return [start, end]
        
        if flag == 1:
            end = len(nums)-1
            return [start,end]
        return [-1, -1]