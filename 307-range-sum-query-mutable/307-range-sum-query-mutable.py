class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.BITree = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.updateTree(i, nums[i])

    def updateTree(self, index: int, val: int) -> None:
        index += 1
        while index <= len(self.nums):
            self.BITree[index] += val
            index += index & (-index)

    def update(self, index: int, val: int) -> None:
        present_val = self.sumRange(0, index) - self.sumRange(0, index-1)
        diff = val - present_val
        index += 1
        while index <= len(self.nums):
            self.BITree[index] += diff
            index += index & (-index)

    def sumRange(self, left: int, right: int) -> int:
        # if left == right:
        #     return self.nums[left]
        # return 0
        res = 0
        index = right + 1
        while index > 0:
            res += self.BITree[index]
            index -= index & (-index)

        s_res = 0
        index = left
        while index > 0:
            s_res += self.BITree[index]
            index -= index & (-index)
        return res - s_res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)