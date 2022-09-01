# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        max_res = -math.inf
        
        def dfs(x, max_res):
            if not x:
                return
            
            if x.val >= max_res:
                res.append(x.val)
            
            max_res = max(max_res, x.val)
            dfs(x.left, max_res)
            dfs(x.right, max_res)
            
        dfs(root, max_res)
        return len(res)
            
            