# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        temp = res[:]
        for i in res:
            if i==val:
                temp.remove(i)
               
        if temp:
            head = ListNode(val=temp[0])
            temp_head = head
        for i in temp[1:]:
            _ = ListNode(val=i)
            temp_head.next = _
            temp_head = _
        return head
            