class Solution:
    def maxSubArray(self, nums):
        combined = [nums[-1]] * len(nums)
        greedy = [nums[-1]] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            # combined.appendleft(combined[0]+nums[i])
            combined[i] = combined[i+1]+nums[i]
            greedy[i] = max(nums[i], greedy[i+1]+nums[i])

        # print(combined)
        # print(greedy)

        return max(max(combined), max(greedy))