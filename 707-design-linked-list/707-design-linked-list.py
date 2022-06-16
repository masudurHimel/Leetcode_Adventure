class Node:
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next
        

class MyLinkedList:

    def __init__(self):
        self.root = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        i = 0
        root = self.root
        while root:
            if i == index:
                return root.val
            else:
                root = root.next
                i += 1
        return -1
            
            
    def addAtHead(self, val: int) -> None:
        temp_root = self.root
        self.root = Node(val, next=temp_root)
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        root = self.root
        prev = root
        while root:
            prev = root
            root = root.next
            
        if prev:
            prev.next = Node(val)
        else:
            self.root = Node(val)
        self.length += 1
        
        
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.length:
            return None
        
        if index == self.length:
            self.addAtTail(val)
            return None
        
        if index == 0:
            self.addAtHead(val)
            return None
        
        i = 0
        root = self.root
        prev = None
        while root:
            if i == index:
                prev.next = Node(val, next=root)
                self.length += 1
                break
            else:
                prev = root
                root = root.next
                i += 1
        return None

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return None
        
        if index == 0:
            self.root = self.root.next
            self.length -= 1
            return None
        
        if index+1 == self.length:
            root= self.root
            prev = root
            t_prev = root
            while root:
                t_prev = prev
                prev = root
                root = root.next
                
            t_prev.next = None
            self.length -= 1
            return None
        
        i = 0
        root = self.root
        prev = None
        while root:
            if i == index:
                prev.next = root.next
                break
            else:
                prev = root
                root = root.next
                i += 1
        self.length -= 1
        return None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)