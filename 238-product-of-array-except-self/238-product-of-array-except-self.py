class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        l, r = [1]*len(nums), [1]*len(nums)
        for i in range(1, len(nums)):
            l[i] = l[i-1] * nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            r[i] = r[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            res.append(l[i]*r[i])
        return res