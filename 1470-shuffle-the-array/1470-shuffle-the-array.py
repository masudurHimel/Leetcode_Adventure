class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # res = []
        x = nums[:n]
        y = nums[n:]
        fx, fy = 0, 0
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = x[fx]
                fx += 1
            else:
                nums[i] = y[fy]
                fy += 1
        return nums