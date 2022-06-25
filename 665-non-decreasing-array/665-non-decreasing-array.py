class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        
#         if len(nums) > 1:
#             if nums[0] > nums[1]:
#                 nums[0] = nums[1]
#                 count += 1
        
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                count+=1
                if i>1 and nums[i-2]>nums[i]:
                    nums[i] = nums[i-1]
            # print(nums)
            if count > 1:
                return False
        return True
            