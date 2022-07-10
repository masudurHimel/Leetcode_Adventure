class SmallestInfiniteSet:

    def __init__(self):
        self.res = set([i for i in range(1,1001)])

    def popSmallest(self) -> int:
        return self.res.pop()

    def addBack(self, num: int) -> None:
        self.res.add(num)
        self.res = set(sorted(self.res))


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)