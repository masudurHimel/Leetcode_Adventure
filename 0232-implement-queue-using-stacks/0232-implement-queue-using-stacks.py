class MyQueue:

    def __init__(self):
        self.lst = deque([])

    def push(self, x: int) -> None:
        self.lst.append(x)
        
    def pop(self) -> int:
        return self.lst.popleft()

    def peek(self) -> int:
        return self.lst[0]

    def empty(self) -> bool:
        return len(self.lst) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()