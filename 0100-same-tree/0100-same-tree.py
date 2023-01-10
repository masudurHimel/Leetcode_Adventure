# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def dfs(self, node):
        if not node:
            self.res.append(None)
            return None
        self.res.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = []
        if not p and not q:
            return True
        
        self.dfs(p)
        a = self.res + []
        self.res = []
        self.dfs(q)
        return a == self.res
        