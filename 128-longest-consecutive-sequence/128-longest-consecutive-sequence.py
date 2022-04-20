class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
            
        nums = sorted(nums)
        count = 1
        max_res = 1
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
                
            if nums[i] - 1 == nums[i-1]:
                # print(nums[i], count)
                count += 1
                max_res = max(count, max_res)
            else:
                max_res = max(count, max_res)
                count = 1
        return max_res