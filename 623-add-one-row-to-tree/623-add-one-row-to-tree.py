# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    val = None
    depth = None
    
    def rec(self, node, level=1):
        if not node: return level-1
        
        if level == self.depth-1:
            if node.left:
                left = TreeNode(self.val, left=node.left)
            else:
                left = TreeNode(self.val)
            if node.right:
                right =  TreeNode(self.val, right=node.right)
            else:
                right = TreeNode(self.val)
            
            node.left = left
            node.right = right
        
        self.rec(node.left, level+1)
        self.rec(node.right, level+1)
    
    def addOneRow(self, root, val, depth):
        if depth == 1:  # Edge Case
            new = TreeNode(val, left=root)
            return new
        
        self.val = val
        self.depth = depth
        self.rec(root)
        
        return root