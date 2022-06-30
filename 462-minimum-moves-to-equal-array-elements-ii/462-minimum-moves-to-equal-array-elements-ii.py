class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums)%2==0:
            pivot = len(nums)//2 - 1
        else:
            pivot = len(nums)//2
            
        res = 0
        for i in range(len(nums)):
            if i == pivot:
                continue
            
            res += abs(nums[i]-nums[pivot])
        
        return res