class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        n = set(nums)
        res = []
        for i in n:
            if i in c and c.get(i) > 1:
                continue
            if i-1 in n or i+1 in n:
                continue
            res.append(i)
        return res