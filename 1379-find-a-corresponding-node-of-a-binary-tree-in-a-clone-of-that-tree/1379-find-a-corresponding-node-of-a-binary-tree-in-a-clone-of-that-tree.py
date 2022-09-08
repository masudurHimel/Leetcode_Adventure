# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    t = None
    res = None
    def dfs(self, node):
        if not node:
            return
        
        if node.val == self.t.val:
            self.res = node
            return
        
        self.dfs(node.left)
        self.dfs(node.right)
        
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.t = target
        self.dfs(cloned)
        return self.res