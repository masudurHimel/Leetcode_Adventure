class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k if len(nums) > k else k%len(nums)
        temp = nums[-k:]
        temp = temp + nums[:-k]
        nums[:] = temp