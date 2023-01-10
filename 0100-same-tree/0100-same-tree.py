# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def levelOrderTraverse(root):
            stack = [root]
            res = []
            
            while stack:
                _ = stack.pop()
                if _ in ["RAN", "LAN"]:
                    res.append(_)
                    continue

                if _.right:
                    stack.append(_.right)
                else:
                    stack.append("RAN")
                if _.left:
                    stack.append(_.left)
                else:
                    stack.append("LAN")
                res.append(_.val)
            return res
        
        if not p and not q:
            return True
        
        if p is None or q is None:
            return False
        
        return levelOrderTraverse(p) == levelOrderTraverse(q)