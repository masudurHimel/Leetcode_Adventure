# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root):
        tree_strs = collections.defaultdict(list)
        res = []

        def dfs(root):
            if root is None:
                return ',_'
            cur_str = dfs(root.left) + dfs(root.right) +  ',' + str(root.val)
            tree_strs[cur_str].append(root)
            return cur_str
        
        dfs(root)
        
        for i in tree_strs:
            if len(tree_strs[i])>1:
                res.append(tree_strs[i][0])
        return res