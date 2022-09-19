# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    
    def dfs(self, node):
        if not node:
            return None

        self.res.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root or (root.left is None and root.right is None):
            return 0
        
        self.res = []
        mres = math.inf
        self.dfs(root)
        self.res.sort()
        for i in range(1, len(self.res)):
            mres = min(mres, abs(self.res[i]-self.res[i-1]))
        return mres