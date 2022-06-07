class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            temp_count = set()
            for j in i:
                if j != ".":
                    temp_count.add(j)
            dot_count = i.count('.')
            if dot_count + len(temp_count) != 9:
                return False
            
        transpose_board = list(zip(*board))
        
        for i in transpose_board:
            temp_count = set()
            for j in i:
                if j != ".":
                    temp_count.add(j)
            dot_count = i.count('.')
            if dot_count + len(temp_count) != 9:
                return False
        
        box_res = x = [[],[],[], [],[],[], [],[],[]]
        
        for i, v in enumerate(board):
            box_res[i//3] += v[0:3]
            box_res[(i+9)//3] += v[3:6]
            box_res[(i+18)//3] += v[6:9]
            
            
        for i in box_res:
            temp_count = set()
            for j in i:
                if j != ".":
                    temp_count.add(j)
            dot_count = i.count('.')
            if dot_count + len(temp_count) != 9:
                return False
            
        
        return True
            