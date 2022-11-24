class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l, rows, cols = len(word), len(board), len(board[0])
        
        def dfs(x, y, d):
            
            if d == l: 
                return True
            else:
                if 0 <= x < cols and 0 <= y < rows and board[y][x] == word[d]:
                    board[y][x], tmp = "", board[y][x]
                    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0,-1)):
                        if dfs(x + dx, y + dy, d + 1): 
                            return True
                    board[y][x] = tmp
        counter, starts = Counter(word), []
        for row in range(rows):
            for col in range(cols):
                counter[board[row][col]] -= 1
                if board[row][col] == word[0]: starts.append((row, col))
        if max(counter.values()) > 0: 
            return False
        for row, col in starts:
            if dfs(col, row, 0): 
                return True