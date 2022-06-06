class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        l = [1]*len(nums)
        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i-1]
        
        temp = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            l[i] = l[i] * temp
            temp *= nums[i]
        
        return l