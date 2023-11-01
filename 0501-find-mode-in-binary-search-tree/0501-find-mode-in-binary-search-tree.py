# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = dict()
    v = []
    def dfs(self, node):
        if not node:
            return None
        self.res[node.val] = self.res.get(node.val, 0) + 1            
        self.dfs(node.left)
        self.dfs(node.right)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.res = dict()
        self.v = []
        self.dfs(root)
        resv = -math.inf
        res = []
        for k, v in self.res.items():
            if v > resv:
                resv = v
        
        for k, v in self.res.items():
            if v == resv:
                res.append(k)
        return res
        