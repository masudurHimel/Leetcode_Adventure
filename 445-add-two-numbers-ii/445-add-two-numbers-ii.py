# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fd, sd = 0,0
        while l1:
            fd = fd *10 + l1.val
            l1 = l1.next
        
        while l2:
            sd = sd *10 + l2.val
            l2 = l2.next
        
        
        res = str(fd + sd)
        head = ListNode(val=res[0])
        res_node = head
        for i in res[1:]:
            _ = ListNode(val = i)
            head.next = _
            head = _
        return res_node
            
        