# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, direction, temp_length):
        if not node:
            return
        
        self.res = max(self.res, temp_length)
        
        if direction == 'left':
            self.dfs(node.right, "right", temp_length+1)
            self.dfs(node.left, "left", 1)
        else:
            self.dfs(node.left, "left", temp_length+1)
            self.dfs(node.right, "right", 1)
            
            
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, "left", 0)
        self.dfs(root, "right", 0)
        return self.res
        