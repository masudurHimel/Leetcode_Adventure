# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        
        while stack:
            temp = []
            v = []
            while stack:
                node = stack.pop()
                v.append(node.left.val if node.left else None)
                v.append(node.right.val if node.right else None)
                
                if node.right:
                    temp.append(node.right)
                if node.left:
                    temp.append(node.left)
            if temp and v[:len(v)//2] != v[len(v)//2:][::-1]:
                return False
            stack += temp
        return True