# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1= ListNode()
        list2= ListNode()
        
        a = list1 
        b = list2
        
        def helper(source, head):
            source.next = head
            source = source.next
            temp = head.next
            source.next = None
            return source, temp
            
        while head:
            if head.val <x:
                a, head = helper(a,head) 
            else:
                b, head = helper(b,head) 
    
        a.next = list2.next
        return list1.next