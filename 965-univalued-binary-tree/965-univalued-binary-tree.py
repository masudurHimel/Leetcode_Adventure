# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node, target_val):
        if not node:
            return True
        
        if target_val != node.val:
            return False
        if not self.dfs(node.left, target_val):
            return False
        if not self.dfs(node.right, target_val):
            return False  
        return True
        
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, root.val)