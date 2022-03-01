class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res = []
        for i in range(len(nums)-2):
            _ = nums[i:i+3]
            if _[0] + _[1] > _[2] and _[0] + _[2] > _[2] and _[1] + _[2] > _[0]:
                return _[0] + _[1] + _[2]
        return 0