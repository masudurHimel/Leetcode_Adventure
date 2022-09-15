# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    target_seq = []
    def dfs(self, node):
        if not node:
            return None
        
        if not node.left and not node.right:
            self.target_seq.append(node.val)
            return None
        
        self.dfs(node.left)
        self.dfs(node.right)
        
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.target_seq = []
        
        self.dfs(root1)
        a = self.target_seq
        self.target_seq = []
        self.dfs(root2)
        b = self.target_seq
        return a == b
        