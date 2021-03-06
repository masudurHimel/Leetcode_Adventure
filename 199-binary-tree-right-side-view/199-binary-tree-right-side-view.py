# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        while queue:
            temp = None
            n = len(queue)
            for i in range(n):
                temp_node = queue.popleft()
                temp = temp_node.val
                if temp_node.left:
                    queue.append(temp_node.left)
                if temp_node.right:
                    queue.append(temp_node.right)
            res.append(temp)
        return res