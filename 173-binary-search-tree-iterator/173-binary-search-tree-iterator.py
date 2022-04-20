# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.iter = 0
        self.tree_list = self.inorderTraversal(root)
    
    def inorderTraversal(self, root):
        res, stack = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    def next(self):
        res = self.tree_list[self.iter]
        self.iter += 1
        return res

    def hasNext(self):
        if (self.iter) < len(self.tree_list):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()