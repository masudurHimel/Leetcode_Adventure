# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = head
        res = []
        
        while head:
            res.append(head.val)
            head = head.next
        
        temp = res[left-1:right]
        res[left-1:right] = temp[::-1]
        
        ind = 0
        
        temp_root = root
        
        while temp_root:
            temp_root.val = res[ind]
            temp_root = temp_root.next
            ind += 1
        return root
        