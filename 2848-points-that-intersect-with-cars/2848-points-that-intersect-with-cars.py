class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        res = set()
        for i, j in nums:
            for m in range(i,j+1):
                res.add(m)
        return len(res)