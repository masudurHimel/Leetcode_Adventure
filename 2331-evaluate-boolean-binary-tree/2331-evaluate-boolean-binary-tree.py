# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node.left is None and node.right is None:
            return bool(node.val)
        
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        
        if node.val == 2:
            if l or r:
                return True
            else:
                return False
        else:
            if l and r:
                return True
            else:
                return False
        
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)