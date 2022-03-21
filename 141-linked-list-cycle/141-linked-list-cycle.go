/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    if head == nil{
        return false
    }

    slow_ptr, fast_ptr := head, head

    for slow_ptr != nil && fast_ptr != nil && fast_ptr.Next != nil{
        slow_ptr = slow_ptr.Next
        fast_ptr = fast_ptr.Next.Next
        if slow_ptr == fast_ptr{
            return true
        }
    }
    return false
}