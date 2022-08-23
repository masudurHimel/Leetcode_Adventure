# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        f = head
        s = head
        while f and f.next:
            res.append(s.val)
            s = s.next
            f = f.next.next
            
        if len(res) == 0:
            return True
        
        while s:
            if s.val == res[-1]:
                res.pop()
            s = s.next
        
        return True if len(res) == 0 else False