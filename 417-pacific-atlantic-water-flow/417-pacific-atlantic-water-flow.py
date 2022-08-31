class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r, c = len(heights), len(heights[0])
        
        def dfs(x, y, prev, valid_set):
            if x < 0 or x == r or y < 0 or y ==c:
                return 
            if (x,y) in valid_set:
                return 
            
            target = heights[x][y]
            if target < prev: 
                return 
        
            valid_set.add((x,y))
            
            dfs(x,y+1, target, valid_set)
            dfs(x,y-1, target, valid_set)
            dfs(x+1,y, target, valid_set)
            dfs(x-1,y, target, valid_set)
            
        
        pacific_valid_set, atlantic_valid_set = set(), set()
        
        for i in range(c):
            dfs(0,i,0,pacific_valid_set)
            
        for i in range(r):
            dfs(i,0,0,pacific_valid_set)
            
        
        for i in range(c):
            dfs(r-1,i,0,atlantic_valid_set)
            
        for i in range(r):
            dfs(i,c-1,0,atlantic_valid_set)
        
        return list(pacific_valid_set & atlantic_valid_set)
            
        
            
        
            
            