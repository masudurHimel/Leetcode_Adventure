class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            return max(
                nums[i] - dp(i + 1, j),
                nums[j] - dp(i, j - 1),
            )

        return dp(0, n - 1) >= 0