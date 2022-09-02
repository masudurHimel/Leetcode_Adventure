# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = [root]
        res = [root.val]
        while stack:
            s = []
            a = []
            while stack:
                curr = stack.pop(0)
                # print(curr.val, end=' ')
                if curr.left:
                    s.append(curr.left)
                    a.append(curr.left.val)
                if curr.right:
                    s.append(curr.right)
                    a.append(curr.right.val)
            
            if len(a) != 0:
                res.append(sum(a)/len(a))
            stack += s

        return res
            
                
            