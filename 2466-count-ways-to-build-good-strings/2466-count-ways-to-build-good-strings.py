class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dp(i):
            if i > high:
                return 0
            return (int(low <= i) + dp(i+one) + dp(i+zero))%(pow(10,9)+7)
        return dp(0)