# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def dfs(self, node, path):
        if not node:
            return path[2:]
        
        l = self.dfs(node.left, path + "->" + str(node.val))
        r = self.dfs(node.right, path + "->" + str(node.val))
        if node.left is None and node.right is None:
            self.res.append(l)
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        self.dfs(root, "")
        return self.res