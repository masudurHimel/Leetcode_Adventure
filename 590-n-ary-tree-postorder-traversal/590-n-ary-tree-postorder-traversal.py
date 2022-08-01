"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    res = []
    def helper(self, root: 'Node'):
        if root:
            for child in root.children:
                self.helper(child)
            self.res.append(root.val)
    
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.helper(root)
        return self.res