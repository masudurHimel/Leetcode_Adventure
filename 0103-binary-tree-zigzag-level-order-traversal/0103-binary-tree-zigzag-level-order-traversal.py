# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = deque([root])
        rev = True
        res = [[root.val]]
        while stack:
            temp = []
            v = []
            while stack:
                node = stack.popleft()
                
                if node.left:
                    temp.append(node.left)
                    v.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    v.append(node.right.val)

            if rev:
                res.append(v[::-1])
                rev = False
            else:
                res.append(v)
                rev = True
            
            stack += temp
        res.pop()
        return res