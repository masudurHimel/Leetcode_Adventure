class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums=list(set(nums))
        nums.sort()
        l,ans = 0,n
        while l<len(nums):
            r = nums[l]+n-1
            i = bisect_right(nums,r)
            ans=min(ans,n-(i-l))
            l+=1
        return ans