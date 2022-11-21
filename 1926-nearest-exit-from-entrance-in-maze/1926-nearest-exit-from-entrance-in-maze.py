class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        queue = collections.deque()
        queue.append((entrance[0], entrance[1], 0))
        seen = set()
        mn = -1
        while queue:
            row, col, step = queue.popleft()
            if mn != - 1 and mn < step:
                continue
            if row >= rows or row < 0 or col >= cols or col < 0:
                continue
            if  maze[row][col] == '+' or (row, col) in seen:
                continue
            seen.add((row, col))
            if not (row == entrance[0] and col == entrance[1]) and (row in [0, rows - 1] or col in [0, cols - 1]):
                return step
            queue.append((row - 1, col, step + 1))
            queue.append((row + 1, col, step + 1))
            queue.append((row, col - 1, step + 1))
            queue.append((row, col + 1, step + 1))
        return -1