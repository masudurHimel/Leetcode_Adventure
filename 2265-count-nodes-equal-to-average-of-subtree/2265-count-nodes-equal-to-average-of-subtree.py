# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def fun(root):
            nonlocal ans
            if not root:
                return [0,0]#returning [sum,nodes]
            left_sum,left_nodes=fun(root.left)
            right_sum,right_nodes=fun(root.right)
            avg=((left_sum+right_sum)+root.val)//(left_nodes+right_nodes+1)
            nodes=left_nodes+right_nodes+1 
            ans+=1 if avg==root.val else 0
            return [(left_sum+right_sum)+root.val,nodes]
        fun(root)
        return ans