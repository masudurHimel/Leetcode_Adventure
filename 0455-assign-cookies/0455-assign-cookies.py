class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        d = dict()
        for i in g:
            d[i] = d.get(i, 0) + 1
        res = 0
        for i in sorted(s):
            for j in d:
                if d.get(j) and j <= i:
                    d[j] -= 1
                    res += 1
                    break
        return res