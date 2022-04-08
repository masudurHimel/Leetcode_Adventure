class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k , self.lst = k, sorted(nums)

    def add(self, val: int) -> int:
        self.lst.append(val)
        self.lst.sort()
        return self.lst[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)