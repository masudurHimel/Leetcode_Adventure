class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max_range = len(nums)
        for i in range(0, max_range+1):
            count = len([j for j in nums if j>=i])
            if count == i:
                return i
        return -1
        