# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
        if not node:
            return
        
        if node in [self.p, self.q]:
            return node
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        if left and right:
            return node
        else:
            return left if left else right
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        return self.dfs(root)
        