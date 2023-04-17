class Solution:
    def maxSubArray(self, nums):
        combined = deque([nums[-1]])
        greedy = deque([nums[-1]])

        for i in range(len(nums) - 2, -1, -1):
            combined.appendleft(combined[0]+nums[i])
            greedy.appendleft(max(nums[i], greedy[0]+nums[i]))

        # print(combined)
        # print(greedy)

        return max(max(combined), max(greedy))