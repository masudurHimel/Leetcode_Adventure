class Solution:
    def smallerNumbersThanCurrent(self, nums):
        x = sorted(nums.copy(), reverse=True)
        for i in enumerate(nums):
            _ = x.count(i[1])
            nums[i[0]] = len(nums) - x.index(i[1]) -1
            if _ > 1:
                nums[i[0]] -= _ -1 
        return nums