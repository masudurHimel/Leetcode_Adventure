class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = defaultdict(int) 
        self.freqs = defaultdict(OrderedDict) 
        self.minFreq = 0 

    def update_freq(self, key, value = None) -> int:
        f = self.items[key]
        v = self.freqs[f].pop(key)
        if value is not None:
            v = value

        self.freqs[f + 1][key] = v
        self.items[key] += 1
        if self.minFreq == f and not self.freqs[f]:
            self.minFreq += 1
        return v

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        return self.update_freq(key)

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return

        if key in self.items:
            self.update_freq(key, value)
        else:
            if len(self.items) == self.capacity:
                self.items.pop(self.freqs[self.minFreq].popitem(last=False)[0])

            self.minFreq = 1
            self.items[key] = 1
            self.freqs[1][key] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)