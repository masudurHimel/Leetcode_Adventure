# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = resNode = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                resNode.next = list1
                list1 = list1.next
            else:
                resNode.next = list2
                list2 = list2.next
            resNode = resNode.next
            
        resNode.next = list1 or list2
        return res.next
    