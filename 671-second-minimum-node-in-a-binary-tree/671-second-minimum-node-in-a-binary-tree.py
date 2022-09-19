# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = set()
    
    def dfs(self, node):
        if not node:
            return None
        self.res.add(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
    
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.res = set()
        self.dfs(root)
        self.res = sorted(list(self.res))
        if len(self.res) <= 1:
            return -1
        return self.res[1]