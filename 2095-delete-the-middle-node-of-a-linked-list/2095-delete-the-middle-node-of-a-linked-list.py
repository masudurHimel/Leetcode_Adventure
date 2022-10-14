# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        target_list = []
        th = head
        while head:
            target_list.append(head.val)
            head = head.next
        target_ind = len(target_list) // 2
        i = 0
        sh = th
        prev = sh
        while sh:
            if i == target_ind:
                if not sh.next:
                    prev.next = sh.next
                    break
                sh.val = sh.next.val
                sh.next = sh.next.next
                break
            prev = sh
            sh = sh.next
            i += 1
        return th