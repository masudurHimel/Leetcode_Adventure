class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            for j, r in enumerate(nums):
                if j == i:
                    continue
                if v + r == target:
                    return [i, j]
        return [0, 0]