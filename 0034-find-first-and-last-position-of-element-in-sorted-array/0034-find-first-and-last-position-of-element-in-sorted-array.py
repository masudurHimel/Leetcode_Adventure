class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res_index = bisect_left(nums, target)
        if res_index >= len(nums):
            return [-1, -1]
        elif nums[res_index] != target:
            return [-1, -1]
        start = res_index
        end = res_index
        res_index += 1
        while res_index < len(nums):
            if nums[res_index] != target:
                break
            end = res_index
            res_index += 1
        return [start, end]