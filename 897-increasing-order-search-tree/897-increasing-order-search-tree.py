# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res , stack = [], []
        node = root
        head = TreeNode(val = root.val)
        res_head = head
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            _ = TreeNode(val=node.val)
            res_head.right = _
            res_head = res_head.right
            
            node = node.right
        
        head = head.right
        
        return head
        