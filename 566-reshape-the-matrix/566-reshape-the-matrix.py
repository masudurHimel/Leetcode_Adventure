class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int):
        total_index = len(mat) * len(mat[0])
        if total_index != r*c:
            return mat
        
        target_list = []
        
        for i in mat:
            for j in i:
                target_list.append(j)
        
        target_ind = 0
        res = []
        for i in range(r):
            res.append([])
            for j in range(c):
                res[i].append(target_list[target_ind])
                target_ind += 1
                
        
        return res
        