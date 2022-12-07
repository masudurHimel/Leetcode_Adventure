# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    high, low = 0, 0
    res = 0
    
    def dfs(self, node):
        if not node:
            return 0
        
        if self.low <= node.val <= self.high:
            self.res += node.val
        
        self.dfs(node.left)
        self.dfs(node.right)
        
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low, self.high = low, high
        self.dfs(root)
        return self.res