# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        e_list = []
        o_list=  []
        temp_head = head
        i = 1
        while head:
            if i % 2 == 0:
                e_list.append(head.val)
            else:
                o_list.append(head.val)
            head = head.next
            i += 1
            
        f_list = o_list + e_list

        head = temp_head
        i = 0
        while temp_head:
            temp_head.val = f_list[i]
            temp_head = temp_head.next
            i += 1
        return head