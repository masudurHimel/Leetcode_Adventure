# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.lst = []
        self.head = head
        temp_head = head
        while temp_head:
            self.lst.append(temp_head.val)
            temp_head = temp_head.next
        
    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()