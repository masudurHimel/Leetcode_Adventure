# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        th = head
        sh = head
        
        total_count = 0
        ft = None
        st = None
        
        while th:
            total_count += 1
            if total_count == k:
                ft = th
            th = th.next
        
        current_count = 0
        while sh:
            current_count += 1
            if current_count + k -1 == total_count:
                st = sh
                break
            sh = sh.next
        
        temp = ft.val
        ft.val = st.val
        st.val = temp
        
        return head