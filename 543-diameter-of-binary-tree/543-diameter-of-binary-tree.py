# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def primary_dfs(self, root):
        if not root:
            return 
        
        self.primary_dfs(root.left)
        self.primary_dfs(root.right)
        
        lc = self.dfs(root.left, 1)
        rc = self.dfs(root.right, 1)
        self.res = max(self.res, lc+rc)
        
    def dfs(self, root, val):
        if not root:
            return val-1
        l = self.dfs(root.left, val+1)
        r = self.dfs(root.right, val+1)
        return max(l,r)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.primary_dfs(root)
        return self.res
        # lc = self.dfs(root.left,1)
        # rc = self.dfs(root.right, 1)
        # return lc + rc
        