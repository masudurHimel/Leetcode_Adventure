# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def dfs(self, node):
        if not node:
            return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        t = node.val
        node.val = abs(l-r)
        return t + l + r
    
    def sumDfs(self, node):
        if not node:
            return 0
        
        self.res += node.val
        l = self.sumDfs(node.left)
        r = self.sumDfs(node.right)
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        self.sumDfs(root)
        return self.res