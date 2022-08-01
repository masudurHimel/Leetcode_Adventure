class RecentCounter:

    def __init__(self):
        self.request = []
        self.range = []
        

    def ping(self, t: int) -> int:
        self.request.append(t)
        self.range = [t-3000, t]
        ind = bisect_left(self.request, t-3000)
        return len(self.request[ind:])


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)