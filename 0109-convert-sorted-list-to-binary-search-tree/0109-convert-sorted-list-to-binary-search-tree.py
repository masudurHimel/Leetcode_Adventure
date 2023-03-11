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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        sl =[]
        while head:
            sl.append(head.val)
            head = head.next
        
        def make_tree(l,i,j):
            m=0
            if i > j:
                return None
            elif i==j:
                return TreeNode(l[i],None,None)
            if (j-i)%2 ==0:
                m=(i+j)//2
            else:
                m=(i+j+1)//2
            return TreeNode(l[m],make_tree(l,i,m-1),make_tree(l,m+1,j))

        return make_tree(sl,0,len(sl)-1)