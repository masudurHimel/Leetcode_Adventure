# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    target_val = None
    def dfs(self,node):
        if not node:
            return True
        
        if self.target_val != node.val:
            return False
        
        if not self.dfs(node.left):
            return False
        if not self.dfs(node.right):
            return False
        
        return True
        
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.target_val = root.val
        return self.dfs(root)