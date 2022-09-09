class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        p = sorted(properties, key=lambda x: (-x[0], x[1]))
        a, d = p[0][0], p[0][1]
        res = 0
        for i, j in p[1:]:
            if i < a and j < d: 
                res += 1
            else: 
                a, d = i, j
        return res