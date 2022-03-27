class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = {}
        sol = []
        for i in range(len(mat)):
            res[i] = mat[i].count(1)
            sol.append(res[i])
        res = sorted(res.items(), key=lambda x: x[1])
        res = [x[0] for x in res]
        return res[:k]