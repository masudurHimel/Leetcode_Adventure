# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return None
        node.left, node.right = self.dfs(node.right), self.dfs(node.left)
        return node

    def invertTree(self, root):
        return self.dfs(root)
        
        