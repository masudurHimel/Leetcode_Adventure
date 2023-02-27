"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def recurse(r, c, n):
            n //= 2
            if n == 0: return Node(grid[r][c], 1)
            tl = recurse(r, c, n)
            tr = recurse(r, c + n, n)
            bl = recurse(r + n, c, n)
            br = recurse(r + n, c + n, n)
            if tl.val == tr.val == bl.val == br.val != 2:
                return Node(tl.val, 1)
            return Node(2, 0, tl, tr, bl, br)
        return recurse(0, 0, len(grid))