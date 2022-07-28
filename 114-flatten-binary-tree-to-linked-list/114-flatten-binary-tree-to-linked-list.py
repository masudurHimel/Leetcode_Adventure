# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
            
        head = root
        stack = deque([head])
        res = deque([])
        
        while stack:
            _ = stack.popleft()
            res.append(_.val)

            if _.right:
                stack.appendleft(_.right)
            if _.left:
                stack.appendleft(_.left)
        
        q = TreeNode(val=res.popleft())
        r = q
        while res:
            q.left = None
            q.right = TreeNode(val=res.popleft())
            q = q.right

        # print(root)
        # print(r)
        
        root.left = None
        root.right = r.right
        
        
        