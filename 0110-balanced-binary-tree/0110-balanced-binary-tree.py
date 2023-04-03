# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, level):
        if not node:
            return level - 1

        l = self.dfs(node.left, level + 1)
        r = self.dfs(node.right, level + 1)

        if l < 0 or r < 0:
            return -1

        if abs(l - r) > 1:
            return -1
        return max(l, r)

    def isBalanced(self, root):
        if not root:
            return True
        if root.left is None and root.right is None:
            return True 
        
        x = self.dfs(root, 0)
        if x < 0:
            return False
        return True