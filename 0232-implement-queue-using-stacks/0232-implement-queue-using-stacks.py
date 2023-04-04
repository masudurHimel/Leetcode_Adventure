class MyQueue:

    def __init__(self):
        self.lst = []
        self.size = 0
        
    def push(self, x: int) -> None:
        self.lst.append(x)
        self.size += 1
        
    def pop(self) -> int:
        i = len(self.lst)
        backup = []
        while i:
            backup.append(self.lst.pop())
            i -= 1
        res = backup.pop()
        i = len(backup)
        while i:
            self.lst.append(backup.pop())
            i -= 1
            
        self.size -= 1
        return res

    def peek(self) -> int:
        i = len(self.lst)
        backup = []
        while i:
            backup.append(self.lst.pop())
            i -= 1
        res = backup.pop()
        backup.append(res)
        i = len(backup)
        while i:
            self.lst.append(backup.pop())
            i -= 1
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