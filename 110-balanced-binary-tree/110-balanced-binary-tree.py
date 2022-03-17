# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def max_height_counter(self, root ):
        max_level = 1
        while root:
            nd, level = root.pop()
            max_level = max(max_level, level)
            if nd.left:
                root.append((nd.left, level+1))
            if nd.right:
                root.append((nd.right, level+1))
        return max_level
            
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [root]
        
        while res:
            head = res.pop()
            if not head:
                continue
            
            max_left = self.max_height_counter([(head.left, 1)]) if head.left else 0
            max_right = self.max_height_counter([(head.right, 1)]) if head.right else 0
            if abs(max_left - max_right) > 1:
                return False
            
            res.append(head.left)
            res.append(head.right)
        return True