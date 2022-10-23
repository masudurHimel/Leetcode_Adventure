class Solution:
    def sumMaker(self,nums):
        nums = [0] + nums
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
    
    def pivotIndex(self, nums: List[int]) -> int:
        primary_nums = self.sumMaker(nums)
        secondary_nums = self.sumMaker(nums[::-1])
        
        p_f, s_f = 1, len(nums)
        # print(primary_nums, secondary_nums)
        while p_f <= len(nums):
            # print(p_f, s_f)
            if primary_nums[p_f-1] == secondary_nums[s_f-1]:
                return p_f-1
            else:
                p_f += 1
                s_f -= 1
        
        return -1