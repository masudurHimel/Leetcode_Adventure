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

        if not l:
            node.left = None
        if not r:
            node.right = None

        if node.val == 1:
            return 1
        if l is None and r is None:
            return 0
        if l or r:
            return 1
        else:
            return 0
        
        
            
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        status = self.dfs(root)
        if status is None:
            return None
        
        if root.val == 0 and root.left is None and root.right is None:
            return None
        
        return root