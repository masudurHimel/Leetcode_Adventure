class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        x = nums[:n]
        y = nums[n:]
        for i in range(len(x)):
            res.append(x[i])
            res.append(y[i])
        return res