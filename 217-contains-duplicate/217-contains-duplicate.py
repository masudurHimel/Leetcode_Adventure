class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _ = set(nums)
        return len(list(_)) < len(nums)