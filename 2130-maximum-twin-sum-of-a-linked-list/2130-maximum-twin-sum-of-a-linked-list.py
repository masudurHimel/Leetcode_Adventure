# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        source = []
        
        while head:
            source.append(head.val)
            head = head.next
        
        res = 0
        n = len(source)
        for i, v in enumerate(source):
            if i > n - 1 - i >= 0:
                res = max(res, source[n-1-i]+v)
        return res