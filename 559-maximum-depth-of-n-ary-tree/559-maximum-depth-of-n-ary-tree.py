"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    res = 0
    def dfs(self, node, height):
        if not node:
            return height
        
        for child in node.children:
            val = self.dfs(child, height + 1)
            self.res = max(self.res, val)
            
        return height
        
        
        
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root, 0)
        return self.res + 1 
        