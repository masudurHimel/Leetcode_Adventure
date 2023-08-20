class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        t_matrix = zip(*grid)
        row_dict = defaultdict(int)
        res = 0
        
        for i in t_matrix:
            row_dict[str(list(i))] += 1
            
        for i in grid:
            if str(i) in row_dict:
                res+=row_dict[str(i)]
        return res
            