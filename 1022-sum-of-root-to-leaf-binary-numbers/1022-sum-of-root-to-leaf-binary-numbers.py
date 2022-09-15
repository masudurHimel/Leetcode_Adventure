# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    f = []
    res = []
    f_res = 0

    def calculateSum(self):
        for i in self.f:
            self.f_res += int(''.join(i), 2)
        return self.f_res

    def dfs(self, node):
        if not node:
            return self.res

        self.res.append(str(node.val))
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        if node.left is None and node.right is None:
            val = deepcopy(l)
            self.f.append(val)
        self.res.pop()
        return self.res

    def sumRootToLeaf(self, root):
        self.f = []
        self.res = []
        self.f_res = 0
        
        _ = self.dfs(root)
        return self.calculateSum()
        