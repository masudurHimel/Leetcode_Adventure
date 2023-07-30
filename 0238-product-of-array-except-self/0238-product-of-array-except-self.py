class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        r = 1
        for i in nums:
            r *= i
            left.append(r)
        
        r = 1
        for i in nums[::-1]:
            r *= i
            right.append(r)
            
        right = right[::-1]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(right[i+1])
            elif i == len(nums)-1:
                res.append(left[i-1])
            else:
                res.append(left[i-1]*right[i+1])
        
        return res