# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def list_to_array(self, root):
        res = []
        while root:
            res.append(root.val)
            root = root.next
        return res
    
    def sortedArrToBST(self, arr):
        if not arr:
            return None
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.left = self.sortedArrToBST(arr[:mid])
        root.right = self.sortedArrToBST(arr[mid+1:])
        return root
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = self.list_to_array(head)
        root = self.sortedArrToBST(arr)
        return root