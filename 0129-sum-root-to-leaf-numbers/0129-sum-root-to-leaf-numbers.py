# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    temp = 0
    def dfs(self, node, r):
        if not node:
            return None
        if not node.left and not node.right:
            self.res.append(r*10+node.val)
            return None
        
        self.dfs(node.left, r*10+node.val)
        self.dfs(node.right, r*10+node.val)
        
        
        return None
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = []
        self.temp = 0
        self.dfs(root, 0)
        # print(self.res)
        return sum(self.res)
        