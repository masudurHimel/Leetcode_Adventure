# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        
        def dfs(root,ind):
            if not root:
                return 
            l.append(ind)
            dfs(root.left,2*ind+1)
            dfs(root.right,2*ind+2)
        
        l=[]
        dfs(root,0)
    
        return max(l)==len(l)-1