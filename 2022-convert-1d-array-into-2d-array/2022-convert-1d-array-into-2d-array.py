class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        
        counter = 0
        
        res = []
        for i in range(m):
            res.append(original[counter:counter+n])
            counter += n
        
        return res