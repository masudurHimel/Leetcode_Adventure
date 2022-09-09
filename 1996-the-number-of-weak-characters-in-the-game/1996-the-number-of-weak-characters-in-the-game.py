class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        p = sorted(properties, key = lambda x: (-x[0], x[1]))
        res = 0
        a, d = p[0][0], p[0][1]
        for i in range(1, len(p)):
            if p[i][0] < a and p[i][1] < d:
                res += 1
            else:
                a, d = p[i][0], p[i][1]
        return res