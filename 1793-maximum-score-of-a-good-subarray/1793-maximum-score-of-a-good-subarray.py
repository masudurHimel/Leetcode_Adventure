class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = right = k
        n = len(nums)
        curmin = curmax = nums[k]
        while left > 0 or right < n-1:
            while left > 0 and nums[left-1] >= curmin:
                left -= 1
            while right < n-1 and nums[right+1] >= curmin:
                right += 1
            if curmax < curmin*(right-left+1):
                curmax = curmin*(right-left+1)
            #how to update curmin? 
            if left > 0 and right < n-1: 
                curmin = max(nums[left-1], nums[right+1])
            elif left == 0 and right < n-1:
                curmin = nums[right+1]
            elif left > 0 and right == n-1:
                curmin = nums[left-1]
        return curmax