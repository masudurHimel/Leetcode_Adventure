# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = None
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res
                