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
    
    def kthSmallest(self, root: Optional[TreeNode], k) -> int:
        self.res = set()
        self.dfs(root)
        self.res = sorted(list(self.res))
        return self.res[k-1]