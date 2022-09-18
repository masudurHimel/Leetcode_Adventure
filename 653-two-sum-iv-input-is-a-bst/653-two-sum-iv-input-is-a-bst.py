# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    stack = []
    def dfs(self, node):
        if not node:
            return None
        
        self.stack.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
        
    def twoSum(self, k):
        c = Counter(self.stack)
        for i in self.stack:
            c[i] = c.get(i) - 1
            if c.get(k-i):
                return True
        return False
        
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.stack = []
        self.dfs(root)
        print(self.stack)
        return self.twoSum(k)