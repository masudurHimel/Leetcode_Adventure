# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def clone(self, tree: TreeNode) -> TreeNode:
        if not tree:
            return None
        new_tree = TreeNode(0)
        new_tree.left = self.clone(tree.left)
        new_tree.right = self.clone(tree.right)
        return new_tree
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        elif N == 1:
            return [TreeNode(0)]
        ret = []
        for i in range(2, N + 1, 2):
            left_branch = self.allPossibleFBT(i - 1)
            right_branch = self.allPossibleFBT(N - i)
            for left_count, left in enumerate(left_branch, 1):
                for right_count, right in enumerate(right_branch, 1):
                    tree = TreeNode(0)
                    tree.left = self.clone(left) if right_count < len(right_branch) else left
                    tree.right = self.clone(right) if left_count < len(left_branch) else right
                    ret.append(tree)
        return ret    