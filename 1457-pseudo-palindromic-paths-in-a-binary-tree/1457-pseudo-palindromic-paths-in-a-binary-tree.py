# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, res):
        if not node:
            return 0

        if node.val in res:
            res.remove(node.val)
        else:
            res.add(node.val)

        if not node.left and not node.right:
            return 1 if len(res) <= 1 else 0

        l = self.dfs(node.left, set(res))
        r = self.dfs(node.right, set(res))

        return l + r

    def pseudoPalindromicPaths(self, root):
        return self.dfs(root, set())