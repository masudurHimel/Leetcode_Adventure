# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    
    def buildTree(self, root):
        if root:
            self.res.append(root.val)
            _ = self.buildTree(root.left)
            _ = self.buildTree(root.right)
        
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        _ = self.buildTree(root)
        return self.res