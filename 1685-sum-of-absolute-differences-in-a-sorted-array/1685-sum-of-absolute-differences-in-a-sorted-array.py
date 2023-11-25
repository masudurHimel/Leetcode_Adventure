class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = list(accumulate(nums))
        suffix = list(accumulate(nums[::-1]))[::-1]

        ans = [i * nums[i] - (prefix[i - 1] if i - 1 >= 0 else 0) +
               (suffix[i + 1] if i + 1 <= n - 1 else 0) - (n - i - 1) * nums[i]
               for i in range(n)]

        return ans
