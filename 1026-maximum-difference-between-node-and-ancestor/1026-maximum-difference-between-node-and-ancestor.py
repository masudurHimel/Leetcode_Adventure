# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode], mn = 1e5, mx = 0) -> int:
        if not root:
            return mx-mn
        mn = min(root.val, mn)
        mx = max(root.val, mx)
        return max(self.maxAncestorDiff(root.left, mn, mx), self.maxAncestorDiff(root.right, mn, mx))