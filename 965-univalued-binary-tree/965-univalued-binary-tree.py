# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        temp = []
        while stack:
            temp = []
            while stack:
                node = stack.pop()
                if node.val != root.val:
                    return False
                if node.right:
                    temp.append(node.right)
                if node.left:
                    temp.append(node.left)
                    
            stack += temp
        return True
                