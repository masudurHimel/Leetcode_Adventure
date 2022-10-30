"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def get_child(self, head):
        if not head:
            return None
        self.res.append(head.val)
        if head.children:
            for child in head.children:
                self.get_child(child)
        else:
            return None

    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.get_child(root)
        print(self.res)
        return self.res