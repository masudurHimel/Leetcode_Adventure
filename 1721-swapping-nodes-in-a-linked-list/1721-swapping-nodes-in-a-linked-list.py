# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        
        res[k-1], res[-k] = res[-k], res[k-1]
        
        res_head = ListNode(val=res[0])
        temp_head = res_head
        for i in res[1:]:
            _ = ListNode(val=i)
            temp_head.next = _
            temp_head = temp_head.next
        return res_head
        
        
        