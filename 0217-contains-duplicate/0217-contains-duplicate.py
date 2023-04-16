class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = {}
        for i in nums:
            c[i] = c.get(i, 0) + 1
            if c.get(i) > 1:
                return True
        return False