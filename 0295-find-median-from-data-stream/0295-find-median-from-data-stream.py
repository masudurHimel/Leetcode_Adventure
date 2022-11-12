
from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.stack = SortedList()
        self.stackLen = 0

    def addNum(self, num: int) -> None:
        self.stack.add(num)
        self.stackLen += 1
        

    def findMedian(self) -> float:
        # print(self.stack)
        if self.stackLen%2 != 0:
            # print(self.stack[self.stackLen//2])
            return self.stack[self.stackLen//2]
        # print((self.stack[self.stackLen//2]+ self.stack[self.stackLen//2 - 1]) / 2)
        return (self.stack[self.stackLen//2]+ self.stack[self.stackLen//2 - 1]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()