class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        marker = dict()
        for i, v in enumerate(nums):
            if target - v in marker:
                return [i, marker[target-v]]
            else:
                marker[v] = i
        return [0, 0]