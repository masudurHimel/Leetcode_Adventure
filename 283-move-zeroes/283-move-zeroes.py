class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        _ = nums.count(0)
        for i in range(_):
            nums.remove(0)
            nums.append(0)