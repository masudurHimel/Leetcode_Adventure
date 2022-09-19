# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        stack = [root]
        parent = {root.val:None}
        level = {root.val: 0}
        l = 0
        res = []
        flag = False
        while stack:
            temp = []
            l += 1
            while stack:
                node = stack.pop()
                
                if node.val == x or node.val == y:
                    flag = True
                
                if flag:
                    break
                
                if node.left:
                    parent[node.left.val] = node.val
                    level[node.left.val] = l
                    temp.append(node.left)
                if node.right:
                    parent[node.right.val] = node.val
                    level[node.right.val] = l
                    temp.append(node.right)
                
            if flag:
                break
            stack += temp
        print(parent)
        print(level)
        if parent.get(x) and parent.get(y) and parent[x] != parent[y] and level[x] == level[y]:
            return True
        return False