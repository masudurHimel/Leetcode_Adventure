class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        land = set((i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if not val)

        def is_closed(x, y):
            if (x, y) not in land: return True
            land.remove((x, y))
            neighbors_closed = is_closed(x+1, y) & is_closed(x-1, y) & is_closed(x, y+1) & is_closed(x, y-1)
            return neighbors_closed and x not in [0, rows-1] and y not in [0, cols-1]

        closed = 0
        while land: 
            closed += is_closed(*next(iter(land)))
        return closed
        