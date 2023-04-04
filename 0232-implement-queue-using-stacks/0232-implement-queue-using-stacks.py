class MyQueue:

    def __init__(self):
        self.lst = []
        self.backup = []
        self.size = 0
        
    def push(self, x: int) -> None:
        self.lst.append(x)
        self.size += 1
        
    def pop(self) -> int:
        if not self.backup:
            while self.lst:
                self.backup.append(self.lst.pop())
        self.size -= 1
        return self.backup.pop()

    def peek(self) -> int:
        if not self.backup:
            while self.lst:
                self.backup.append(self.lst.pop())
        res = self.backup.pop()
        self.backup.append(res)
        return res

    def empty(self) -> bool:
        if self.size:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()