class Solution:
    @cache
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int):
        if any([startRow < 0, startColumn < 0, startRow >= m, startColumn >= n]):
            return 1
        if not maxMove:
            return 0
        
        possible_paths = [(startRow + 1, startColumn), (startRow - 1, startColumn), (startRow, startColumn + 1), (startRow, startColumn - 1)]
        return sum(self.findPaths(m, n, maxMove-1, tempRow, tempColumn) for tempRow, tempColumn in possible_paths) % (10 ** 9 + 7)
        