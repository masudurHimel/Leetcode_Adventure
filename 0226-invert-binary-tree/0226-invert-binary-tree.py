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
        
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        
        node.left = r
        node.right = l
        
        return node
        
        return None
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return root
        