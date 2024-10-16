# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, temp_list):
        if not root:
            return
        elif root.val == self.target:
            self.res += 1
            
        for i in range(len(temp_list)):
            temp_list[i] = temp_list[i] + root.val
            if temp_list[i] == self.target:
                self.res += 1
        
        self.dfs(root.left, temp_list+[root.val])
        self.dfs(root.right, temp_list+[root.val])
            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0
        self.target = targetSum
        self.dfs(root, [])
        return self.res