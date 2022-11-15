# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return 0
        
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        
        return 1 + l+r
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)