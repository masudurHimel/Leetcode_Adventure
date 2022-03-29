# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = []
        stack.append(root)
        res = 0
        
        while stack:
            v = stack.pop()
            res += v.val if v.val >= low and v.val <=high else 0
            for i in [v.left, v.right]:
                if i:
                    stack.append(i)
        
        
        return res