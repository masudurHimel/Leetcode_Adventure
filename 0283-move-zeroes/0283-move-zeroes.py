class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = nums.count(0)
        t = c
        while t:
            nums.remove(0)
            t -= 1
        nums += [0]*c
        