# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    
    def helper(self,root):
        if root:
            self.helper(root.left)
            self.helper(root.right)
            self.res.append(root.val)
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.helper(root)
        return self.res    