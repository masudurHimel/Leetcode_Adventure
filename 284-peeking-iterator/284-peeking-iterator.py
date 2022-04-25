# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.next_val = -1

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.next_val == -1:
            val = self.it.next()
            self.next_val = val
            return val
        return self.next_val
        

    def next(self):
        """
        :rtype: int
        """
        if self.next_val == -1:
            return self.it.next()
        
        val = self.next_val
        self.next_val = -1
        return val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.next_val == -1:
            return self.it.hasNext()
        else:
            return True
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].