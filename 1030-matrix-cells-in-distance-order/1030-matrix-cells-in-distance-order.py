class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res_hash = {}
        max_counter = -1
        for i in range(rows):
            for j in range(cols):
                dist = abs(i-rCenter) + abs(j-cCenter)
                max_counter = max(dist, max_counter)
                res_hash[dist] = res_hash.get(dist, []) + [[i,j]]
        
        res = []
        for i in range(max_counter+1):
            temp_res = res_hash.get(i, None)
            if temp_res:
                res += temp_res
        return res
        