# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = math.inf
    
    def dfs(self, node, level):
        if not node:
            return math.inf
        if not node.left and not node.right:
            return level + 1
        
        
        
        
        l = self.dfs(node.left, level+1)
        r = self.dfs(node.right, level+1)
        self.res = min([self.res,l,r])
        return min(l,r)
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.res = math.inf
        self.res = min(self.res, self.dfs(root, 0))
        return self.res