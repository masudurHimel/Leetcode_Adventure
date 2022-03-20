# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]):
        if not head:
            return head
        res = []
        while head:
            res.append(head.val)
            head = head.next
            
        linked_res = ListNode(val=res[len(res)-1])
        temp_res = linked_res
        for i in range(len(res)-2, -1, -1):
            _ = ListNode(val=res[i])
            temp_res.next = _
            temp_res = temp_res.next
            
        return linked_res