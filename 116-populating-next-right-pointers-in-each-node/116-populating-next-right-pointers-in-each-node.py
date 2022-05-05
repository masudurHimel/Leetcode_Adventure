"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        res = []
        res_node = root
        tmp_node = root
        tmp_root = root
        res_t = []
        while root:
            res_t.append(root.val)
            if root.left:
                res += [root.left, root.right]
            
            if res:
                root = res.pop(0)
            else:
                break
        
        res_node = Node(val=res_t[0])
        tmp_node = res_node
        
        for i in range(1, len(res_t)):
            if i+1 and (not(i+1 & (i))):
                tmp_node.next = Node(val='#')
                tmp_node = tmp_node.next
            tmp_node.next = Node(val=res_t[i])
            tmp_node = tmp_node.next
        
        return res_node
            