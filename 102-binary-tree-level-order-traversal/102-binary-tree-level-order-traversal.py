# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        res = []
        temp_node = root
        temp_list = [temp_node]
        
        while temp_list:
            temp = []
            n = len(temp_list)
            for i in range(n):
                res_node = temp_list.pop(0)
                temp.append(res_node.val)
                if res_node.left: 
                    temp_list.append(res_node.left)
                if res_node.right: 
                    temp_list.append(res_node.right)
            res.append(temp)

        return res
            