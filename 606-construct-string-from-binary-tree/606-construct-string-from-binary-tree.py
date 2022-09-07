# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return None

        l = self.dfs(node.left)
        r = self.dfs(node.right)

        if r and not l:
            l = '()'
        elif not l:
            l = ''
        else:
            l = f'({l})'
        if not r:
            r = ''
        else:
            r = f'({r})'

        return f'{node.val}{l}{r}'

    def tree2str(self, root):
        res = self.dfs(root)
        return res