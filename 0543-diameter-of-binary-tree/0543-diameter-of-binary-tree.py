# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = -math.inf
    def dfs(self, node):
        if not node:
            return 0
        
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        
        self.res = max(self.res, l+r)
        return max(l, r) + 1
        
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res