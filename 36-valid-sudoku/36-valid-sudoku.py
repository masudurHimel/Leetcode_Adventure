class Solution:
    
    def validSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            temp_count = set()
            for j in i:
                if j != ".":
                    temp_count.add(j)
            dot_count = i.count('.')
            if dot_count + len(temp_count) != 9:
                return False
            
        return True
        
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        primary_check = self.validSudoku(board)
        if not primary_check:
            return False
            
        transpose_board = list(zip(*board))
        
        col_check = self.validSudoku(transpose_board)
        if not col_check:
            return False
        
        
        box_res = x = [[],[],[], [],[],[], [],[],[]]
        
        for i, v in enumerate(board):
            box_res[i//3] += v[0:3]
            box_res[(i+9)//3] += v[3:6]
            box_res[(i+18)//3] += v[6:9]
            
        box_check = self.validSudoku(box_res)
        if not box_check:
            return False
        
        return True
            