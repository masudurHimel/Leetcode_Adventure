# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        res.append([root1, root2])
        while res:
            if root1 is None:
                return root2
            _ = res.pop(0)
            if _[1] is None:
                continue
            _[0].val += _[1].val

            if _[0].left is None:
                _[0].left = _[1].left
            else:
                res.append([_[0].left, _[1].left])
            if _[0].right is None:
                _[0].right = _[1].right
            else:
                res.append([_[0].right, _[1].right])
        return root1
            