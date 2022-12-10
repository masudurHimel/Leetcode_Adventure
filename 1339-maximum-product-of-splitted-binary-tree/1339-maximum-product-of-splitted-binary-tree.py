# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0
        self.max_product = 0
        MOD = 10**9+7

        def getSum(root):
            if root is None:
                return 0
            self.total_sum += root.val
            left = getSum(root.left)
            right = getSum(root.right)
            root.val += left + right
            return root.val

        getSum(root)

        def dfs(root):
            if root is None:
                return
            
            self.max_product = max(self.max_product, (self.total_sum-root.val) * root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        return self.max_product % MOD