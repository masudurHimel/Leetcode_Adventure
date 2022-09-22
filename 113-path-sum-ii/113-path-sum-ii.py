# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def dfs(self, node, ls):
        if not node:
            return None
        
        ls.append(node.val)
        
        if not node.left and not node.right:
            self.res.append(ls)
            return None
        
        self.dfs(node.left, []+ls)
        self.dfs(node.right, []+ls)
        
        
        return True
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        
        self.dfs(root, [])
        res = []
        for i in self.res:
            if sum(i) == targetSum:
                res.append(i)
        return res