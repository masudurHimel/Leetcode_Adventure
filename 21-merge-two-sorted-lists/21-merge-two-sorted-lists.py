# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        res = []
        if not list1:
            return list2
        elif not list2:
            return list1
        
        while list1 or list2:
            if list1:
                res.append(list1.val)
                list1 = list1.next
            elif list2:
                res.append(list2.val)
                list2 = list2.next
        res.sort()
        if res:
            base = ListNode(val=res[0])
            res_node = base
            for i in res[1:]:
                base.next = ListNode(val=i)
                base = base.next
        return res_node
            
        