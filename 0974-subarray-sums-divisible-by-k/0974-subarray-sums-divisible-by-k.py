class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        d = dict()
        d[0] = 1
        n = len(nums)
        sum = 0
        ans = 0
        for i in range(n):
            sum += nums[i]
            ans += d.get(sum % k, 0)
            d[sum % k] = d.get(sum % k, 0) + 1
        return ans