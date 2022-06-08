class Solution:
    def threeSum(self, nums: List[int]):
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            l = i+1
            h = len(nums) -1
            target = 0 - nums[i]
            
            while(l<h):
                if nums[l] + nums[h] > target:
                    h = h-1
                elif nums[l] + nums[h] < target:
                    l = l+1
                else:
                    res.add((nums[i], nums[l], nums[h]))
                    l += 1
                    h -= 1
            
        
        return res
            