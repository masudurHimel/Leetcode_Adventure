class LRUCache:

    def __init__(self, capacity: int):
        self.data = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        data = self.data.get(key, None)
        if data is not None:
            self.data.move_to_end(key)        
            return data
        return -1
        

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        self.data.move_to_end(key)
        
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)