# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    targetSum = None

    def dfs(self, node, prev, has):
        if not node:
            if prev == self.targetSum and has:
                return True
            return False
        
        if node.right is None and node.left is None:
            h = True
        else:
            h = False

        l = self.dfs(node.left, node.val + prev, has=h)
        r = self.dfs(node.right, node.val + prev, has=h)

        if l or r:
            return True
        return False

    def hasPathSum(self, root, targetSum):
        self.targetSum = targetSum
        if not root:
            return 0
        if root.val == self.targetSum and (root.left is None or root.right is None) and not (root.left is None and root.right is None):
            return False
        if root.left and root.right:
            h = True
        else:
            h = False
        return self.dfs(root, 0, h)