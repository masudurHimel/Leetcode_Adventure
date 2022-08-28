class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        res = defaultdict(list)
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                res[row-col].append(mat[row][col])
        
        
        for k in res.keys():
            res[k] = sorted(res[k])
        
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                mat[row][col] = res[row-col].pop(0)
        
        return mat