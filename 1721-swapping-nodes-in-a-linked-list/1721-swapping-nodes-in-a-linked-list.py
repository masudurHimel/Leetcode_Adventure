# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ft, st = None, None
        index_map = dict()
        ind = 0
        th = head
        while head:
            ind += 1
            index_map[ind] = head
            head = head.next
        
        ft = index_map[k]
        st = index_map[ind-k+1]
        temp = ft.val
        ft.val = st.val
        st.val = temp
        return th