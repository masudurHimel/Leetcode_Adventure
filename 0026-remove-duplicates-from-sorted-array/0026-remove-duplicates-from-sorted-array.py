class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            nums[:] = sorted(list(set(nums)))
        