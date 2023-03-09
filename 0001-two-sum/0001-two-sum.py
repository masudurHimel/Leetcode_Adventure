class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = defaultdict(list)
        for i, v in enumerate(nums):
            ref[v].append(i)
        l, r = 0, len(nums)-1
        nums = sorted(nums)
        while l <= r:
            s = nums[l] + nums[r]
            if s == target:
                return [ref[nums[l]].pop(), ref[nums[r]].pop()]
            elif s > target:
                r -= 1
            else:
                l += 1
        return []