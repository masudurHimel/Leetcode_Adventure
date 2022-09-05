"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        stack = [root]
        res = []
        while stack:
            temp = []
            a = []
            while stack:
                node = stack.pop(0)
                temp.append(node.val)
                
                for children in node.children:
                    a.append(children)
            stack += a
            res.append(temp)
        return res