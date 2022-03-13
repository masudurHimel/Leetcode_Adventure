class Solution:
    def removeElement(self, nums: List[int], val: int):
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)