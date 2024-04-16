class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = defaultdict(int)
        
        for i in nums:
            if c.get(i, 0) >= 1:
                return True
            else:
                c[i] += 1
        return False