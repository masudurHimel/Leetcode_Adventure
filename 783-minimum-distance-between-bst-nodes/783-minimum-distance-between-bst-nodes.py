# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sortedcontainers
class Solution:
    res = []
    
    def dfs(self, node):
        if not node:
            return None

        self.res.add(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
        
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if not root or (root.left is None and root.right is None):
            return 0
        
        self.res = sortedcontainers.SortedList()
        mres = math.inf
        self.dfs(root)
        for i in range(1, len(self.res)):
            mres = min(mres, abs(self.res[i]-self.res[i-1]))
        return mres