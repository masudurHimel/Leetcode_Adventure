class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = sum(nums[:3])
        if res > target:
            return res
        res = sum(nums[-3:])
        if res < target:
            return res
        
        for i in range(len(nums)):
            x = i+1
            y = len(nums) - 1
            
            while x < y:
                temp_sum = nums[i] + nums[x] + nums[y]
                
                if abs(target-temp_sum) < abs(target-res):
                    res = temp_sum
                elif temp_sum < target:
                    x += 1
                else:
                    y -= 1
            
        return res
                    
                
                