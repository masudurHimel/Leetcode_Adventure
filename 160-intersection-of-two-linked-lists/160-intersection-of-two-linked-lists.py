# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        x, y = headA, headB
        while x is not y:
            if x is None:
                x = headB
            else:
                x = x.next
            
            if y is None:
                y = headA
            else:
                y = y.next
        return x